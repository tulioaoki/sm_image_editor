import cv2
import numpy as np

def toPutGlasses(IMAGE_NAME,value,imgNumber):

    face = cv2.imread(IMAGE_NAME, -1)

    extraW = 0
    extraH = 0

    if(value == 1): # Slider esta no meio
          
        oculos = cv2.imread("./images/Stickers/tugLife.png", -1)

    elif(value == 0):

        oculos = cv2.imread("./images/Stickers/oculosDeSol.png", -1)

    elif(value == 2):

        img  = cv2.imread(IMAGE_NAME)    
        imagem = "./images/FuncaoDeEdicao/edited" + "{}".format(imgNumber) + "{}".format(".jpg")
        cv2.imwrite(imagem , img)   # Save the image
        return imagem
    
    elif(value == 3):

        oculos = cv2.imread("./images/Stickers/oculosMulher.png", -1)
        
    else:
        oculos = cv2.imread("./images/Stickers/oculosNormal.png", -1)

    ## For oculos
    
    gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
    eyes_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +  "haarcascade_eye_tree_eyeglasses.xml")
    
    vetor = [0] * 8
    i = 0

    if(eyes_cascade == None):

        img  = cv2.imread(IMAGE_NAME)    
        imagem = "./images/FuncaoDeEdicao/edited" + "{}".format(imgNumber) + "{}".format(".jpg")
        cv2.imwrite(imagem , img)   # Save the image
        return imagem

    else:

        eyes = eyes_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in eyes:

            vetor[i] = x
            vetor[i+1] = w
            vetor[i+2] = y
            vetor[i+3] = h

            i = i + 4

        face = cv2.cvtColor(face, cv2.COLOR_BGR2BGRA)

        if(vetor[0] == 0):
            
            img  = cv2.imread(IMAGE_NAME)    
            imagem = "./images/FuncaoDeEdicao/edited" + "{}".format(imgNumber) + "{}".format(".jpg")
            cv2.imwrite(imagem , img)   # Save the image
            return imagem

        if(vetor[3] <= vetor[7]):

            altura = vetor[7]
            inicioY = vetor[6]

        elif(vetor[3] > vetor[7]):
            altura = vetor[3]
            inicioY = vetor[2]

        if(vetor[0] < vetor[4]): # O Segundo olho (olho da direita)  foi reconhecido pela segunda iteração 
            
            comprimento = (vetor[4] + vetor[5]) - vetor[0]   
            inicioX = vetor[0] # começa no x do olho esquerdo
            
        elif(vetor[0] > vetor[4]): # O Segundo olho (olho da direita)  foi reconhecido pela primeira iteração
            
            comprimento = (vetor[0] + vetor[1]) - vetor[4]   
            inicioX = vetor[4]

        if(value == 3):

            comprimento = comprimento + 40   # Comprimento do oculos
            altura = altura + 60          # Altura do oculos

        else:
            comprimento = comprimento + 20   # Comprimento do oculos
            altura = altura + 40          # Altura do oculos

        
        oculos = cv2.resize(oculos, (comprimento,altura))
        w, h, c = oculos.shape

        
    
       

    for i in range(0, w):       # Operação Linha a Linha 
        
        for j in range(0, h):

            if (oculos[i, j][3] != 0):

                if( (inicioX + i) <= (vetor[4] + vetor[5]) ):

                    if(value == 3):

                        face[ (inicioY - 30 )+ i ,  inicioX- 20 + j] = oculos[i, j]

                    else:

                        face[ (inicioY - 20 )+ i ,  inicioX- 10 + j] = oculos[i, j]


    imagem = "./images/FuncaoDeEdicao/edited" + "{}".format(imgNumber) + "{}".format(".jpg")
    cv2.imwrite(imagem, face)   # Save the image
    return imagem




