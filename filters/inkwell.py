import cv2
import numpy as np


def toInkwell(img, hue = 1, saturation = 1, contrast = 1.3, brightness = -30): # OK
	img = cv2.imread(img)  # Take the image
	img = hue_saturation(img,hue,saturation)
	img = brightness_contrast(img, contrast, brightness)
	img = grayscale(img)
	cv2.imwrite("./images/PhotoInEdition/filtered.jpg", img) 
	return "./images/PhotoInEdition/filtered.jpg"
    
def brightness_contrast(img, alpha = 1.0, beta = 0):
    img_contrast = img * alpha
    img_bright = img_contrast + beta
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

def grayscale(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img_gray    

