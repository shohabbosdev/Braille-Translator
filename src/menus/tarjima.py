import streamlit as st
from PIL import Image
import cv2
import numpy as np
from ultralytics import YOLO
import torch
import logging
import time
from typing import Tuple
from braille_symbols import BrailleConverter  # BrailleConverter import

# Logging konfiguratsiyasi
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('app.log'), logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

class BrailleDetector:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = self._load_model()

    @staticmethod
    @st.cache_resource(ttl=3600)
    def _load_model():
        try:
            model = YOLO("models/yolov8_braille.pt")
            return model
        except Exception as e:
            logger.error(f"YOLO modelini yuklashda xato: {str(e)}")
            return None

    def preprocess_image(self, image: Image.Image) -> np.ndarray:
        try:
            img_array = np.array(image)
            img_array = cv2.fastNlMeansDenoisingColored(img_array, None, 10, 10, 7, 21)
            lab = cv2.cvtColor(img_array, cv2.COLOR_RGB2LAB)
            l, a, b = cv2.split(lab)
            clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
            cl = clahe.apply(l)
            processed_img = cv2.merge((cl, a, b))
            processed_img = cv2.cvtColor(processed_img, cv2.COLOR_LAB2RGB)
            return processed_img
        except Exception as e:
            logger.error(f"Rasmni qayta ishlashda xato: {str(e)}")
            return None

    def detect_braille(self, image: np.ndarray, confidence: float = 0.6, overlap: float = 0.25) -> Tuple[np.ndarray, np.ndarray]:
        try:
            if self.model is None:
                raise ValueError("YOLO modeli yuklanmagan")

            self.model.overrides["conf"] = confidence
            self.model.overrides["iou"] = overlap
            results = self.model.predict(image)
            boxes = results[0].boxes
            annotated_image = results[0].plot()
            return boxes, annotated_image
        except Exception as e:
            logger.error(f"Brayl belgilarini aniqlashda xato: {str(e)}")
            return None, None

    def draw_bounding_boxes(self, image: np.ndarray, boxes) -> np.ndarray:
        try:
            if boxes is None:
                return image
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                label = f"{box.cls[0].item()}"
                cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
            return image
        except Exception as e:
            logger.error(f"Qutilarni chizishda xato: {str(e)}")
            return image

    def extract_braille_symbols(self, boxes) -> str:
        braille_symbols = []
        try:
            for box in boxes:
                braille_value = int(box.cls[0].item())
                braille_pattern = format(braille_value, '06b')  # Braille belgisini binar shaklda olish
                braille_symbols.append(braille_pattern)
            braille_converter = BrailleConverter()
            translated_text = ''.join([braille_converter.convert_braille_to_chars(symbol) for symbol in braille_symbols])
            logger.info(f"Aniqlangan braille belgilar (binar): {braille_symbols}")
            logger.info(f"Tarjima qilingan matn: {translated_text}")
            return translated_text
        except Exception as e:
            logger.error(f"Braille belgilarini ajratishda xato: {str(e)}")
            return ""

class StreamlitApp:
    def __init__(self):
        self.detector = BrailleDetector()
        self.converter = BrailleConverter()
        self.setup_ui()

    def setup_ui(self):
        st.markdown("<h1 style='text-align:center;'>Brayl Tarjimon</h1>", unsafe_allow_html=True)
        with st.sidebar:
            self.confidence = st.slider("Aniqlik", 0.1, 1.0, 0.6)
            self.overlap = st.slider("O'xshashlik", 0.1, 1.0, 0.25)

    def process_image(self, image: Image.Image) -> None:
        try:
            col1, col2 = st.columns(2)
            with col1:
                st.write("Asl rasm")
                st.image(image)
            processed_image = self.detector.preprocess_image(image)
            if processed_image is None:
                st.error("Rasmni qayta ishlashda xatolik yuz berdi")
                return
            start_time = time.time()
            with st.spinner("Aniqlash jarayoni..."):
                boxes, annotated_image = self.detector.detect_braille(processed_image, self.confidence, self.overlap)
                if boxes is None:
                    st.error("Brayl belgilarini aniqlab bo'lmadi")
                    return
                detection_time = time.time() - start_time
                st.metric(label="Aniqlash vaqti (soniya)", value=round(detection_time, 2))
                st.metric(label="Aniqlik foizi", value=f"{self.confidence * 100:.0f}%")
                with col2:
                    st.write("Aniqlangan belgilar va qutilar")
                    annotated_with_boxes = self.detector.draw_bounding_boxes(annotated_image, boxes)
                    st.image(annotated_with_boxes)
                braille_symbols = self.detector.extract_braille_symbols(boxes)
                st.write("Aniqlangan so'zlar:", braille_symbols)


        except Exception as e:
            logger.error(f"Rasmni qayta ishlashda xatolik: {str(e)}")
            st.error("Xatolik yuz berdi. Iltimos, qaytadan urinib ko'ring.")

def app():
    app = StreamlitApp()
    uploaded_file = st.file_uploader("Rasm yuklang", type=["jpg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        app.process_image(image)

if __name__ == "__main__":
    app()
