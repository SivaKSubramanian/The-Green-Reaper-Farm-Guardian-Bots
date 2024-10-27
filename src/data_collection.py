import json
from datetime import datetime

class DataCollection:
    def __init__(self):
        self.data_log = []

    def log_data(self, image_data, pest_detected, pest_type):
        data_entry = {
            "timestamp": datetime.now().isoformat(),
            "image_data": image_data,
            "pest_detected": pest_detected,
            "pest_type": pest_type
        }
        self.data_log.append(data_entry)
        print(f"Logged data: {data_entry}")

    def save_log(self, filename="data/processed_data/detection_log.json"):
        with open(filename, "w") as f:
            json.dump(self.data_log, f, indent=4)
        print(f"Data saved to {filename}")
