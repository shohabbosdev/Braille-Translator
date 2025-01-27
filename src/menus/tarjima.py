import streamlit as st
from ultralytics import YOLO
from PIL import Image
from random import randrange
import numpy as np
import json
import cv2
import io
from scipy import ndimage
import tempfile
import time
import requests
import random

@st.cache_resource
def load_model():
    return YOLO("models/yolov8_braille.pt")
 
@st.cache_data
def load_braille_map():
    with open("models/braille_maps.json", "r", encoding="utf-8") as fl:
        return json.load(fl)

model = load_model()
braille_map = load_braille_map()

# Kategoriya ro'yxati
category_lists = [
    'happiness', 'age', 'alone', 'amazing', 'anger', 'architecture', 'art', 
    'attitude', 'beauty', 'best', 'birthday', 'business', 'car', 'change', 
    'communication', 'computers', 'cool', 'courage', 'dad', 'dating', 'death', 
    'design', 'dreams', 'education', 'environmental', 'equality', 'experience', 
    'failure', 'faith', 'family', 'famous', 'fear', 'fitness', 'food', 
    'forgiveness', 'freedom', 'friendship', 'funny', 'future', 'god', 'good', 
    'government', 'graduation', 'great', 'health', 'history', 'home', 'hope', 
    'humor', 'imagination', 'inspirational', 'intelligence', 'jealousy', 
    'knowledge', 'leadership', 'learning', 'legal', 'life', 'love', 'marriage', 
    'medical', 'men', 'mom', 'money', 'morning', 'movies', 'success'
]

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

# Tanlangan kategoriyaga oid iqtibos olish funksiyasi
def select_category(category):
    response = requests.get(f'{st.secrets['QUOTE_URL']}{category}', headers={'X-Api-Key': f"{st.secrets['OCR_QUOTE_API']}"})
    if response.status_code == 200:
        quote = response.json()[0]["quote"]
        author = response.json()[0]["author"]
        return [quote, author]
    else:
        st.error(f"Xatolik: {response.status_code}, {response.text}")

# Rasmni matnga aylantirish funksiyasi
def image_to_text(image):
    files = {'image': image}
    headers = {'X-Api-Key': f"{st.secrets['OCR_QUOTE_API']}"}
    try:
        response = requests.post(st.secrets['OCR_URL'], headers=headers, files=files)
        if response.status_code == 200:
            text_results = response.json()
            if text_results:
                extracted_text = " ".join([item["text"] for item in text_results])
                return extracted_text
            else:
                return "Hech qanday matn topilmadi."
        else:
            return f"Xatolik: {response.status_code}, {response.text}"
    except Exception as e:
        return f"Xatolik: {e}"

def app():
    st.markdown("# ✅ :rainbow[Rasmli brayl yozuvini oddiy o'zbekcha alifboga o'tkazish]", unsafe_allow_html=True)

    with st.sidebar:
        with st.expander(":orange[Natijalarni sozlang]", icon='⚙️'):
            confidence = st.slider("Aniqlik", 0.1, 1.0, 0.6)
            overlap_threshold = st.slider("O'xshashlik", 0.1, 1.0, 0.25)
        burish = st.checkbox("Tasvirni to'g'rilash")
        st.image('src/image.png', width=150)
        st.markdown("👁 :rainbow[O'zbekcha Brayl tarjimon]")

    # Tasodifiy kategoriya tanlash
    category = category_lists[randrange(len(category_lists))]
    # st.markdown(f"> :blue[{select_category(category)[0]}]")
    st.html(f'<div align="right">📕 {select_category(category)[1]} </div>')
        
      
    brailleTab1, brailleTab2 = st.tabs(["1\. :orange[Brayldan tasviridan matnga o'tkazish]", "2\. :green[Lotincha rasmdan matnga o'tkazish]"])
    with brailleTab1:
        braille_image = st.file_uploader(":camera: Rasmni tanlang", type=["png", "jpg", "jpeg"], label_visibility='hidden')
        qator1, qator2 = st.columns(2)
        if braille_image:
            image = load_image(braille_image, burish)
            qator1.image(image, caption="Asl rasm", width=300)
            with st.spinner('Algoritm ishlamoqda...'):
                try:
                    start_time = time.time()
                    
                    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_file:
                        image.save(temp_file.name)
                        temp_file.close()

                        predict = model.predict(temp_file.name, conf=confidence, iou=overlap_threshold)
                        res_plotted = predict[0].plot()[:, :, ::-1]
                        qator2.image(res_plotted, caption="Segmentlangan tasvir", width=300)
                        
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
    with brailleTab2:
        uploaded_image = st.file_uploader("Rasmni yuklang...", type=['jpg', 'png'])
        
        # Rasm yuklangan yoki yuklanmaganligini tekshirish va vaqtni hisoblash
        if uploaded_image:
            rowing1, rowing2 = st.columns([2, 4])
            rowing1.image(uploaded_image, caption="Dastlabki rasm")

            # Matn ajratish vaqti
            with st.spinner("Siz yuborgan tasvirdan matnlar ajratib olinayabdi. Iltimos, kuting..."):
                start_time = time.time()
                extracted_text = image_to_text(uploaded_image)
                end_time = time.time()
                elapsed_time = f"{(end_time - start_time):.2f} sekund"

            # Natijani ko'rsatish
            rowing2.text_area("Natija...", value=extracted_text, height=150)
            st.metric("Aniqlashga sarflangan vaqt:",value=elapsed_time, delta=random.randrange(-15,15))
            st.html("<hr />")
        else:
            st.write("Fayl yuklash tugmasini bosing")
if __name__ == "__main__":
    app()
