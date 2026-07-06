import cv2
import numpy as np


def load_image(path):
    image = cv2.imread(path)
    if image is None:
        raise ValueError(f"Unable to read image: {path}")
    return preprocess(image)


def preprocess(image):
    image = cv2.resize(image, (480, 480), interpolation=cv2.INTER_AREA)
    image = cv2.GaussianBlur(image, (3, 3), 0)
    return image


def histogram_similarity(image_a, image_b):
    hsv_a = cv2.cvtColor(image_a, cv2.COLOR_BGR2HSV)
    hsv_b = cv2.cvtColor(image_b, cv2.COLOR_BGR2HSV)

    hist_a = cv2.calcHist([hsv_a], [0, 1], None, [50, 60], [0, 180, 0, 256])
    hist_b = cv2.calcHist([hsv_b], [0, 1], None, [50, 60], [0, 180, 0, 256])
    cv2.normalize(hist_a, hist_a, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    cv2.normalize(hist_b, hist_b, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

    correlation = cv2.compareHist(hist_a, hist_b, cv2.HISTCMP_CORREL)
    return float(np.clip((correlation + 1) / 2, 0, 1))
