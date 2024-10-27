import random

class PestDetection:
    def __init__(self, model_path="models/pest_detection_model.pth"):
        print("Loading pest detection model...")
        self.model_path = model_path

    def detect_pest(self, image_data):
        # Placeholder for AI model prediction
        pest_detected = random.choice([True, False])
        pest_type = random.choice(["Aphid", "Moth", "Beetle"]) if pest_detected else "None"
        print(f"Pest detected: {pest_detected}, Type: {pest_type}")
        return pest_detected, pest_type
