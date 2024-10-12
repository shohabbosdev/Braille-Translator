import streamlit as st         
from ultralytics import YOLO
from PIL import Image
import os
import numpy as np
import io
import tempfile
import time
import json
import numpy as np
import torch
from find_rotate import detect_and_rotate

# UI elements
st.markdown("<h1 style='text-align:center;'>❄️ Brayl tarjimon</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center; color: orange;'>1-darajali Brayl alifbosini aniqlash dasturi</h4>", unsafe_allow_html=True)

maps_path = {
    "O'zbekcha":"models/braille_maps.json",
     "Ruscha":"models/russian_maps.json",
     "Inglizcha": "models/english_maps.json",
     }

with st.expander("Natijalarni sozlash uchun meni bosing!", icon='⛈'):
    confidence = st.slider("Aniqlik", 0.1, 1.0, 0.6) 
    overlap_threshold = st.slider("O'xshashlik", 0.1, 1.0, 0.25)
burish = st.checkbox("Tasvirni to'g'rilash")

st.markdown("<p><code>Eslatma: Faqat so'z va iboralarni qayta ishlash bilan cheklangan.</code></p>", unsafe_allow_html=True)

select_language = st.selectbox("Lug'atni tanlang", options=maps_path, placeholder="Select language")

upload_image = st.file_uploader(":camera: Rasmni tanlang", type=["png", "jpg", "jpeg"], label_visibility='hidden')

@st.cache_resource()
def load_model():
    try:
        model = YOLO("models/yolov8_braille.pt")
        model.overrides["conf"] = confidence 
        model.overrides["iou"] = overlap_threshold
        return model
    except Exception:
        st.error("Model yuklanmadi. Brauzerni yangilang.",icon="🚨")
        return None

def load_image(upload):
    try:
        if upload is None:
            st.error("Tasvir yuklanmadi. Iltimos, fayl yuklang.",icon="🚨")
            return None

        image = Image.open(upload)
        
        if burish:
            rotated_image = detect_and_rotate(image)
            if rotated_image is None:
                st.error("Tasvirni qayta ishlashda muammo yuz berdi.",icon="🚨")
                return None
            return rotated_image.convert("RGB")
        else:
            return image.convert("RGB")
    except Exception as e:
        st.error(f"Tasvirni yuklashda xato: {str(e)}",icon="🚨")
        return None

def create_download_button(image):
    buf = io.BytesIO()
    image.save(buf, format="JPEG")
    return st.download_button(
        label="Skanerlangan rasmni yuklab olish",
        data=buf.getvalue(),
        file_name="image_result.jpg",
        mime="image/jpeg"
    )

def get_percentage(confidences):
    mean = np.mean(confidences)
    return f"{mean * 100:.2f}"

model = load_model()

col2, col3 = st.columns(2)
with st.sidebar:
    st.image('src/image.png', width=150)
    st.markdown("<p style='font-weight: bold; color: rgba(25,25,225, 0.8);'>👁 O'zbekcha Brayl tarjimon</p>",unsafe_allow_html=True)
    
    st.divider()
    st.link_button("Men bilan bog'lanish",'https://t.me/shohabbosdev',type='secondary', icon="💻", use_container_width=True)


select_language = maps_path["O'zbekcha"] if select_language=="O'zbekcha"else maps_path["Inglizcha"] if select_language=="Inglizcha" else maps_path["Ruscha"]

def convert_to_braille_unicode(str_input: str, path: str = select_language) -> str:
    with open(path, "r", encoding='utf-8') as fl:
        data = json.load(fl)

    if str_input in data.keys():
        str_output = data[str_input]

        print(f"Brayldan unicodega konvertatsiya natijasi: {str_output}")
    return str_output


def parse_xywh_and_class(boxes: torch.Tensor) -> list:

    # copy values from troublesome "boxes" object to numpy array
    new_boxes = np.zeros(boxes.shape)
    new_boxes[:, :4] = boxes.xywh.numpy()  # first 4 channels are xywh
    new_boxes[:, 4] = boxes.conf.numpy()  # 5th channel is confidence
    new_boxes[:, 5] = boxes.cls.numpy()  # 6th channel is class which is last channel

    # sort according to y coordinate
    new_boxes = new_boxes[new_boxes[:, 1].argsort()]

    # find threshold index to break the line
    y_threshold = np.mean(new_boxes[:, 3]) // 2
    boxes_diff = np.diff(new_boxes[:, 1])
    threshold_index = np.where(boxes_diff > y_threshold)[0]

    # cluster according to threshold_index
    boxes_clustered = np.split(new_boxes, threshold_index + 1)
    boxes_return = []
    for cluster in boxes_clustered:
        # sort according to x coordinate
        cluster = cluster[cluster[:, 0].argsort()]
        boxes_return.append(cluster)

    return boxes_return

image = load_image(upload_image) if upload_image else load_image("src/Braille.jpg")
col2.write("Asl rasm")
col2.image(image)

with st.spinner('Algoritm ishlamoqda...'):
    start_timer = time.time()
    try:
        file_path = tempfile.mktemp(suffix=".jpg") if upload_image else 'src/Braille.jpg'
        if upload_image:
            with open(file_path, "wb") as img_file:
                img_file.write(upload_image.getbuffer())

        predict = model.predict(file_path, exist_ok=True)
        res_plotted = predict[0].plot()[:, :, ::-1]
        col3.write("Segmentlangan tasvir: ")
        col3.image(res_plotted)

        boxes = predict[0].boxes
        confidences = boxes.conf.numpy()
        percent = get_percentage(confidences)
        list_boxes = parse_xywh_and_class(boxes)

        for box_line in list_boxes:
            str_left_to_right = "".join(convert_to_braille_unicode(model.names[int(each_class)]) for each_class in box_line[:, -1])
            st.write(f"<code>{str_left_to_right}</code>",unsafe_allow_html=True)

        st.write(f"Aniqlik: <span style='color: blue;'>{percent}%<span>",unsafe_allow_html=True)
        create_download_button(Image.fromarray(res_plotted))
        st.success(f'Muvaffaqiyatli bajarildi! \nIshlash vaqti {time.time() - start_timer:.2f} sekund.', icon="✅")
    except Exception as e:
        st.error(f"Xatolik xabari:\n {e}",icon="🚨")