from drone_control import DroneControl
from pest_detection import PestDetection
from data_collection import DataCollection

def main():
    drone = DroneControl()
    detector = PestDetection()
    logger = DataCollection()

    for image_data in drone.run():
        pest_detected, pest_type = detector.detect_pest(image_data)
        logger.log_data(image_data, pest_detected, pest_type)
        if len(logger.data_log) >= 5:  # Save log every 5 entries for simplicity
            logger.save_log()

if __name__ == "__main__":
    main()
