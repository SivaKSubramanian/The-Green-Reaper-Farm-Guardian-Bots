import random
import time

class DroneControl:
    def __init__(self):
        print("Initializing drone control system...")

    def navigate(self):
        print("Drone is navigating the crop field...")

    def capture_image(self):
        print("Capturing image of the crop field.")
        image_data = f"image_{random.randint(1, 100)}.jpg"
        return image_data

    def run(self):
        while True:
            self.navigate()
            captured_image = self.capture_image()
            time.sleep(5)  # Capture image every 5 seconds
            yield captured_image
