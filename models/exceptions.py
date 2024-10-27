class BrailleTranslatorError(Exception):
    """Base exception for BrailleTranslator application"""
    pass

class ModelLoadError(BrailleTranslatorError):
    """Raised when model loading fails"""
    pass

class ImageProcessingError(BrailleTranslatorError):
    """Raised when image processing fails"""
    pass

class DetectionError(BrailleTranslatorError):
    """Raised when braille detection fails"""
    pass