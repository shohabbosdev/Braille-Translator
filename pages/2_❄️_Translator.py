import streamlit as st         
from ultralytics import YOLO
from PIL import Image
import os
import numpy as np
import io
import tempfile
import time
import decimal

from arrange_boxes import convert_to_braille_unicode, parse_xywh_and_class
from find_rotate import detect_and_rotate

# UI elements
st.markdown("<h1 style='text-align: center;'>Brayl tarjimon</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: grey;'>1-darajali Brayl alifbosini aniqlash dasturi</h3>", unsafe_allow_html=True)
st.text("")

with st.expander("Natijalarni sozlash uchun meni bosing!"):
    confidence = st.slider("Aniqlik", 0.1, 1.0, 0.6) 
    overlap_threshold = st.slider("O'xshashlik", 0.1, 1.0, 0.25)
burish = st.checkbox("Tasvirni to'g'rilash")

st.markdown("<p style='text-align: center;'><code>Eslatma: Faqat so'z va iboralarni qayta ishlash bilan cheklangan.</code></p>", unsafe_allow_html=True)
upload_image = st.file_uploader(":camera: Rasmni tanlang", type=["png", "jpg", "jpeg"], label_visibility='hidden')

@st.cache_resource()
def load_model():
    try:
        model = YOLO("models/yolov8_braille.pt")
        model.overrides["conf"] = confidence 
        model.overrides["iou"] = overlap_threshold
        return model
    except Exception:
        st.error("Model yuklanmadi. Brauzerni yangilang.")
        return None

def load_image(upload):
    try:
        # Agar yuklangan fayl bo'lmasa, xatolik chiqaramiz
        if upload is None:
            st.error("Tasvir yuklanmadi. Iltimos, fayl yuklang.")
            return None

        # Agar fayl yuklangan bo'lsa, uni BytesIO formatiga o'girib ochamiz
        image = Image.open(upload)
        
        if burish:
            rotated_image = detect_and_rotate(image)
            if rotated_image is None:
                st.error("Tasvirni qayta ishlashda muammo yuz berdi.")
                return None
            return rotated_image.convert("RGB")
        else:
            return image.convert("RGB")
    except Exception as e:
        st.error(f"Tasvirni yuklashda xato: {str(e)}")
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
    return decimal.Decimal(mean * 100).quantize(decimal.Decimal('0.00'))

model = load_model()

col2, col3 = st.columns(2)

# Load and display the image
with col2:
    image = load_image(upload_image) if upload_image else load_image("src/sample_image.jpg")
    col2.write("Asl rasm")
    col2.image(image)

with col3:
    with st.spinner('Algoritm ishlamoqda...'):
        start_timer = time.time()
        try:
            file_path = tempfile.mktemp(suffix=".jpg") if upload_image else 'src/sample_image.jpg'
            if upload_image:
                with open(file_path, "wb") as img_file:
                    img_file.write(upload_image.getbuffer())

            predict = model.predict(file_path, exist_ok=True)
            res_plotted = predict[0].plot()[:, :, ::-1]
            col3.write("Algoritmi natijasi: ")
            col3.image(res_plotted)

            boxes = predict[0].boxes
            confidences = boxes.conf.numpy()
            percent = get_percentage(confidences)
            list_boxes = parse_xywh_and_class(boxes)

            for box_line in list_boxes:
                str_left_to_right = "".join(convert_to_braille_unicode(model.names[int(each_class)]) for each_class in box_line[:, -1])
                st.write(f"<code>{str_left_to_right}</code>",unsafe_allow_html=True)

            st.write(f"Aniqlik: {percent}%")
            create_download_button(Image.fromarray(res_plotted))
            st.success(f'Muvaffaqiyatli bajarildi! \nIshlash vaqti {time.time() - start_timer:.2f} sekund.', icon="✅")
        except Exception:
            st.error("Qayta urining. Brayl belgilarining ko‘rinishini tekshiring yoki pastdagi slayder yordamida aniqlashni sozlang.")
