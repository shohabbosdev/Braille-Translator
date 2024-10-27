import torch
import numpy as np
from ultralytics import YOLO
import streamlit as st
from models.config import DEFAULT_CONFIG
from PIL import Image
from typing import Tuple, List, Optional

class BrailleDetector:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self._load_models()
        
    @staticmethod
    @st.cache_resource(ttl=DEFAULT_CONFIG["MODEL"]["CACHE_TTL"])
    def _load_yolo_model():
        try:
            model = YOLO(DEFAULT_CONFIG["MODEL"]["YOLO_PATH"])
            return model
        except Exception as e:
            st.error(f"YOLO modelini yuklashda xato: {str(e)}")
            return None

    def _load_models(self):
        try:
            self.detection_model = self._load_yolo_model()
            if self.detection_model:
                self.detection_model.to(self.device)
        except Exception as e:
            st.error(f"Modellarni yuklashda xato: {str(e)}")

    def preprocess_image(self, image: Image.Image) -> np.ndarray:
        try:
            # Maksimal o'lchamni cheklash
            max_size = DEFAULT_CONFIG["IMAGE"]["MAX_SIZE"]
            ratio = min(max_size/image.width, max_size/image.height)
            if ratio < 1:
                new_size = (int(image.width * ratio), int(image.height * ratio))
                image = image.resize(new_size, Image.LANCZOS)
            
            return np.array(image)
        except Exception as e:
            st.error(f"Rasm preprocessing xatosi: {str(e)}")
            return None

    def detect_braille(
        self,
        image: np.ndarray,
        confidence: float = DEFAULT_CONFIG["MODEL"]["CONFIDENCE_THRESHOLD"],
        overlap: float = DEFAULT_CONFIG["MODEL"]["OVERLAP_THRESHOLD"]
    ) -> Tuple[Optional[List], Optional[np.ndarray]]:
        try:
            if self.detection_model is None:
                raise ValueError("YOLO modeli yuklanmagan")
                
            self.detection_model.overrides["conf"] = confidence
            self.detection_model.overrides["iou"] = overlap
            
            results = self.detection_model.predict(image)
            boxes = results[0].boxes
            annotated_image = results[0].plot()
            
            return boxes, annotated_image
        except Exception as e:
            st.error(f"Brayl aniqlashda xato: {str(e)}")
            return None, None