import logging
from typing import Optional
import numpy as np
from PIL import Image
import cv2
from models.config import *
def setup_logging(config: dict) -> None:
    """
    Logging konfiguratsiyasini o'rnatish
    """
    logging.basicConfig(
        level=config["LOGGING"]["LEVEL"],
        format=config["LOGGING"]["FORMAT"],
        handlers=[
            logging.FileHandler(config["LOGGING"]["FILE"]),
            logging.StreamHandler()
        ]
    )

def preprocess_image(
    image: Image.Image,
    max_size: int = DEFAULT_CONFIG["IMAGE"]["MAX_SIZE"]
) -> np.ndarray:
    """
    Rasmni qayta ishlash
    
    Args:
        image: PIL Image obyekti
        max_size: Maksimal rasm o'lchami
        
    Returns:
        Qayta ishlangan numpy array
    """
    try:
        # O'lchamni optimallashtirish
        ratio = min(max_size/image.width, max_size/image.height)
        if ratio < 1:
            new_size = (int(image.width * ratio), int(image.height * ratio))
            image = image.resize(new_size, Image.LANCZOS)
        
        # Kontrast va yorug'likni optimizatsiya qilish
        img_array = np.array(image)
        lab = cv2.cvtColor(img_array, cv2.COLOR_RGB2LAB)
        l, a, b = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
        cl = clahe.apply(l)
        processed = cv2.merge((cl,a,b))
        processed = cv2.cvtColor(processed, cv2.COLOR_LAB2RGB)
        
        return processed
    except Exception as e:
        raise ImageProcessingError(f"Rasm preprocessing xatosi: {str(e)}")