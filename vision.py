# Minimal stub — replace with real CV/ML model
def detect_pollution(image):
    """
    Simulated detection. In a real system you'd run an object detection model (YOLO/Mask R-CNN)
    and return bounding boxes and classes. Here we return a dummy result.
    """
    return [
        {"type": "plastic_bottle", "confidence": 0.92, "location": [100, 50, 200, 150]},
        {"type": "microplastic_cluster", "confidence": 0.58, "location": [300, 210, 340, 240]},
    ]
