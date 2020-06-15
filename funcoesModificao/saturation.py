from scipy.interpolate import UnivariateSpline
import cv2 
import numpy as np
    

def spreadLookupTable(x, y):
    
    spline = UnivariateSpline(x, y)
    return spline(range(256))


def saturaration(IMAGE_NAME ,value, imgNumber):

    
    img  = cv2.imread(IMAGE_NAME)

    imagem = "./images/FuncaoDeEdicao/edited" + "{}".format(imgNumber) + "{}".format(".jpg")
    
    if(value >= 127):

        multiplicador = value - 127
        result = multiplicador * 0.32
        valor = round(result)

        c_h, c_s, c_v = cv2.split(cv2.cvtColor(img,  cv2.COLOR_RGB2HSV))

        increaseLookupTableSa = spreadLookupTable([0, 64, 128, 192, 256], [0, (64+valor), (128+valor), (192+valor), 256] )
        
        c_s = cv2.LUT(c_s, increaseLookupTableSa).astype(np.uint8)
    
        final = cv2.cvtColor(cv2.merge((c_h, c_s, c_v)), cv2.COLOR_HSV2RGB)
        cv2.imwrite(imagem , final)   # Save the image
        return "./images/FuncaoDeEdicao/edited" + "{}".format(imgNumber) + "{}".format(".jpg")
        

    elif(value < 127):
        
        multiplicador = 127 - value
        result = multiplicador * 0.342
        valor = round(result)
        
        c_h, c_s, c_v = cv2.split(cv2.cvtColor(img,  cv2.COLOR_RGB2HSV))
        
        decreaseLookupTable = spreadLookupTable([0, 64, 128, 192, 256], [0, (64-valor), (128-valor), (192-valor), (256-valor)])
        
        c_s = cv2.LUT(c_s, decreaseLookupTable).astype(np.uint8)
        

        final = cv2.cvtColor(cv2.merge((c_h, c_s, c_v)), cv2.COLOR_HSV2RGB)
        cv2.imwrite(imagem , final)   # Save the image
        
        return "./images/FuncaoDeEdicao/edited" + "{}".format(imgNumber) + "{}".format(".jpg")
        
        
#img1 = saturaration("./images/PublishedPhoto/fotoTirada.jpg" , 255 , 1)

#img1= cv2.imread(img1)

#img2 = saturaration("./images/PublishedPhoto/fotoTirada.jpg" , 0 , 2)

#img2= cv2.imread(img2)

#img0 = cv2.imread("./images/PublishedPhoto/fotoTirada.jpg")

#cv2.imshow("Foto Original", img0)
#cv2.imshow("Foto Saturada UP", img1)
#cv2.imshow("Foto Saturada DOWN", img2)



#k = cv2.waitKey(0)     #  Receberá o valor do keyboard (esc == 27)
#if (k == 27):  
#    cv2.destroyAllWindows() # Fecha a janela
    