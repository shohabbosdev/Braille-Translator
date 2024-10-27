import torch
from ultralytics import YOLO
import streamlit as st
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model
from transformers import pipeline
from typing import Optional, Tuple, List

class ModelManager:
    """Model yuklash va boshqarish uchun klass"""
    
    def __init__(self, config: dict):
        self.config = config
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        
    @st.cache_resource(ttl=DEFAULT_CONFIG["MODEL"]["CACHE_TTL"])
    def load_yolo_model(self) -> Optional[YOLO]:
        """YOLOv8 modelini yuklash"""
        try:
            model = YOLO("models/yolov8_braille.pt")
            return model
        except Exception as e:
            raise ModelLoadError(f"YOLO modelini yuklashda xato: {str(e)}")

    @st.cache_resource(ttl=DEFAULT_CONFIG["MODEL"]["CACHE_TTL"])
    def load_resnet_model(self) -> Optional[Model]:
        """ResNet modelini yuklash"""
        try:
            base_model = ResNet50(weights='imagenet', include_top=False)
            x = GlobalAveragePooling2D()(base_model.output)
            x = Dense(1024, activation='relu')(x)
            predictions = Dense(len(self.config["LANGUAGES"]), activation='softmax')(x)
            return Model(inputs=base_model.input, outputs=predictions)
        except Exception as e:
            raise ModelLoadError(f"ResNet modelini yuklashda xato: {str(e)}")

    @st.cache_resource(ttl=DEFAULT_CONFIG["MODEL"]["CACHE_TTL"])
    def load_nlp_model(self) -> Optional[pipeline]:
        """NLP modelini yuklash"""
        try:
            return pipeline("text2text-generation", model="t5-base")
        except Exception as e:
            raise ModelLoadError(f"NLP modelini yuklashda xato: {str(e)}")