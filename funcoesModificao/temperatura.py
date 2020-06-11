import cv2
import numpy as np

def converte_temp(IMAGE_NAME, self):
    img_rgb = cv2.imread(IMAGE_NAME)
    c_r, c_g, c_b = cv2.split(img_rgb)
    c_r = cv2.LUT(c_r, self.incr_ch_lut).astype(np.uint8)
    c_b = cv2.LUT(c_b, self.decr_ch_lut).astype(np.uint8)
    img_rgb = cv2.merge((c_r, c_g, c_b))
    return img_rgb