import cv2
import numpy as np
from PIL import Image
    
def get_limits(color):
    c = np.uint8([[color]])  # BGR values
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    hue = hsvC[0][0][0]  # Get the hue value

    # Handle red hue wrap-around
    if hue >= 165:  # Upper limit for divided red hue
        lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upperLimit = np.array([180, 255, 255], dtype=np.uint8)
    elif hue <= 15:  # Lower limit for divided red hue
        lowerLimit = np.array([0, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)
    else:
        lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)

    return lowerLimit, upperLimit

def detect_colour(frame, color):
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerLimit, upperLimit = get_limits(color=color)

    mask = cv2.inRange(hsv_frame, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    image_with_contours = frame.copy()

    cv2.drawContours(image_with_contours, contours, -1, (0, 255, 0), 2) # Green color, thickness 2

    # if bbox is not None:
    #     x1, y1, x2, y2 = bbox
    #     frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
    # return frame
    return image_with_contours


if __name__ == "__main__":
    
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        color = [255, 0, 0]
        frame = detect_colour(frame, color)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()

    cv2.destroyAllWindows()