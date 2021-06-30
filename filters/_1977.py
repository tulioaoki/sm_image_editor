import cv2
import numpy as np

def to1977(img, hue = 1, saturation = 1.3, contrast = 1.1, brightness = -30): 
    img = cv2.imread(img)  # Take the image
    img = hue_saturation(img, hue, saturation)
    img = brightness_contrast(img, contrast, brightness)
    img = vignette(img,243,106,188,0.3)
    cv2.imwrite("./images/PhotoInEdition/filtered.jpg", img)   # Save the image
    return "./images/PhotoInEdition/filtered.jpg"


def brightness_contrast(img, alpha = 1.0, beta = 0):
    img_contrast = img * (alpha)
    img_bright = img_contrast + (beta)
    img_bright = np.clip(img_bright,0,255)
    img_bright = img_bright.astype(np.uint8)
    return img_bright

def hue_saturation(img_rgb, alpha = 1, beta = 1):
    img_hsv = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2HSV)
    hue = img_hsv[:,:,0]
    saturation = img_hsv[:,:,1]
    hue = np.clip(hue * alpha ,0,179)
    saturation = np.clip(saturation * beta,0,255)
    img_hsv[:,:,0] = hue
    img_hsv[:,:,1] = saturation
    img_transformed = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
    return img_transformed

def vignette(img,r,g,b,a):
    color = img.copy()
    color[:,:,0] = b
    color[:,:,1] = g
    color[:,:,2] = r
    res = cv2.addWeighted(img,1-a,color,a,0)
    return res
