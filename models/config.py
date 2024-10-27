import logging
from pathlib import Path

DEFAULT_CONFIG = {
    "IMAGE": {
        "MAX_SIZE": 1024,
        "DEFAULT_SIZE": (640, 640),
        "FORMATS": [".jpg", ".jpeg", ".png"],
    },
    "MODEL": {
        "CACHE_TTL": 86400,  # 24 soat
        "CONFIDENCE_THRESHOLD": 0.6,
        "OVERLAP_THRESHOLD": 0.25,
        "YOLO_PATH": "models/yolov8_braille.pt"
    },
    "LANGUAGES": {
        "O'zbekcha": "models/braille_maps.json",
        "Ruscha": "models/russian_maps.json",
        "Inglizcha": "models/english_maps.json",
    },
    "LOGGING": {
        "LEVEL": logging.INFO,
        "FORMAT": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        "FILE": "app.log",
    }
}