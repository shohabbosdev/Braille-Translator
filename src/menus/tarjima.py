import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import json
import cv2
import io
from scipy import ndimage
import tempfile
import time

@st.cache_resource
def load_model():
    return YOLO("models/yolov8_braille.pt")
 
@st.cache_data
def load_braille_map():
    with open("models/braille_maps.json", "r", encoding="utf-8") as fl:
        return json.load(fl)

model = load_model()
braille_map = load_braille_map()

def convert_to_braille_unicode(str_input):
    return braille_map.get(str_input, "")

def load_image(upload, burish=False):
    if not upload:
        st.error("Tasvir yuklanmadi. Iltimos, fayl yuklang.", icon="🚨")
        return None
    try:
        image = Image.open(upload)
        if image.mode != "RGB":
            image = image.convert("RGB")
        if burish:
            return detect_and_rotate(image)
        return image
    except Exception as e:
        st.error(f"Tasvirni yuklashda xato: {str(e)}", icon="🚨")
        return None

def detect_and_rotate(image):
    try:
        img_before = np.array(image)
        img_gray = cv2.cvtColor(img_before, cv2.COLOR_RGB2GRAY)
        img_edges = cv2.Canny(img_gray, 100, 100, apertureSize=3)
        lines = cv2.HoughLinesP(img_edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=5)
        if lines is None:
            return image
        angles = [np.degrees(np.arctan2(y2 - y1, x2 - x1)) for line in lines for x1, y1, x2, y2 in line]
        median_angle = np.median([angle for angle in angles if 45 <= abs(angle) <= 135])
        img_rotated = ndimage.rotate(img_before, median_angle)
        return Image.fromarray(img_rotated.astype(np.uint8))
    except Exception as e:
        st.error(f"Xato: {e}", icon="🚨")
        return image

def create_download_button(image):
    buf = io.BytesIO()
    image.save(buf, format="JPEG")
    st.download_button(
        label="Skanerlangan rasmni yuklab olish",
        data=buf.getvalue(),
        file_name="image_result.jpg",
        mime="image/jpeg"
    )

def parse_xywh_and_class(boxes):
    new_boxes = np.zeros(boxes.shape)
    new_boxes[:, :4] = boxes.xywh.numpy()
    new_boxes[:, 4] = boxes.conf.numpy()
    new_boxes[:, 5] = boxes.cls.numpy()
    new_boxes = new_boxes[new_boxes[:, 1].argsort()]
    y_threshold = np.mean(new_boxes[:, 3]) // 2
    boxes_diff = np.diff(new_boxes[:, 1])
    threshold_index = np.where(boxes_diff > y_threshold)[0]
    boxes_clustered = np.split(new_boxes, threshold_index + 1)
    boxes_return = []
    for cluster in boxes_clustered:
        cluster = cluster[cluster[:, 0].argsort()]
        boxes_return.append(cluster)
    return boxes_return

def app():
    st.markdown("# ✅ :rainbow[Rasmli brayl yozuvini oddiy o'zbekcha alifboga o'tkazish]", unsafe_allow_html=True)

    with st.sidebar:
        with st.expander("Natijalarni sozlash uchun meni bosing!", icon='⛈'):
            confidence = st.slider("Aniqlik", 0.1, 1.0, 0.6)
            overlap_threshold = st.slider("O'xshashlik", 0.1, 1.0, 0.25)
        burish = st.checkbox("Tasvirni to'g'rilash")
        st.image('src/image.png', width=150)
        st.markdown("👁 :rainbow[O'zbekcha Brayl tarjimon]")

    upload_image = st.file_uploader(":camera: Rasmni tanlang", type=["png", "jpg", "jpeg"], label_visibility='hidden')
    qator1, qator2 = st.columns(2)
    if upload_image:
        image = load_image(upload_image, burish)
        qator1.image(image, caption="Asl rasm")
        with st.spinner('Algoritm ishlamoqda...'):
            try:
                start_time = time.time()
                
                with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_file:
                    image.save(temp_file.name)
                    temp_file.close()

                    predict = model.predict(temp_file.name, conf=confidence, iou=overlap_threshold)
                    res_plotted = predict[0].plot()[:, :, ::-1]
                    qator2.image(res_plotted, caption="Segmentlangan tasvir")
                    
                    confidences = predict[0].boxes.conf.numpy()
                    percent = f"{np.mean(confidences) * 100:.2f}%"
                    elapsed_time = time.time() - start_time
                    elapsed_time_text = f"{elapsed_time:.4f}"
                    
                    # Braille matnini bitta qatorli qilib birlashtirish
                    braille_text = "".join(
                        "".join(convert_to_braille_unicode(model.names[int(each_class)]) for each_class in box_line[:, -1])
                        for box_line in parse_xywh_and_class(predict[0].boxes)
                    )
                    
                    # Bitta text_input bilan natijani ko'rsatish
                    qator1.text_input("Natija", braille_text)
                    
                    # Aniqlik va vaqtni ko'rsatish
                    qator2.metric("Aniqlik:", percent, delta_color='normal')
                    qator2.metric("Tasvirni aniqlash vaqti(s):", elapsed_time_text, delta_color='inverse')
                    
                    with qator1:
                        create_download_button(Image.fromarray(res_plotted))
                    st.success(f'Muvaffaqiyatli bajarildi!')
            except Exception as e:
                st.error(f"Xatolik xabari:\n {e}", icon="🚨")

if __name__ == "__main__":
    app()
