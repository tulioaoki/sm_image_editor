import cv2 as cv


def segmentar(IMAGE_NAME):
    Imagem = IMAGE_NAME
    # 1.Selecionar um valor estimado para T (ponto intermediário
    # entre os valores mínimos e máximo de uma imagem
    # 2. Segmentar a imagem usando T
    #   R1 >= T e R2 < T
    # 3. Calcular a média das intensidades dos pixels em cada região
    #  media1 = media(R1) e media2 = media(R2)
    # 4. Calcular o novo valor de T ,
    #   T = (media1+ media2)/2
    # 5. Repetir os passo 2 a 4 até que a diferença em T em
    # sucessivas iterações seja menor que um T0 préestabelecido

    # 0: Binary
    # 1: Binary Inverted
    # 2: Threshold Truncated
    # 3: Threshold to Zero
    # 4: Threshold to Zero Inverted
    
    # Load the image

    img = cv.imread(Imagem)
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # Convert it to grayscale

      
    max_binary_value = 255
    
    height = img.shape[0]  # Numero de linha da matriz
    width = img.shape[1]   # Numero de colunas da matriz

    qtdPixelImage = height * width # Numero total de pixels que a imagem possui


    qtdMenorT = 0          # Armazena quantos pixels estão abaixo do limiar
    qtdMaiorT = 0          # Armazena quantos pixels estão a cima do limiar
    
    menorNivelCinza = 0
    MaiorNivelCinza = 0
    pegueiMenorNivel = False
    dst = None

    somaNivelDeCinzaMaior = 0
    somaNivelDeCinzaMenor = 0

    limiarAnterior = None  # Primeiro valor de T
    limiarAtual = 255        # Segundo valor de T (m1 + m2)/2

    qtdNiveCinza_Pixel = [0] * 256       # Vetor de inteiros que guardará a quantidade de pixels por nivel de cinza
    qtdInteracao = 0

    for i in range (height): # Percorrer a Matriz linha por linha 
        for j in range (width):            
            
            nivelDeCinza = img[i][j]
            qtdAntes = qtdNiveCinza_Pixel[nivelDeCinza]
            soma = qtdAntes + 1
            qtdNiveCinza_Pixel[nivelDeCinza] = soma
    
  
    # Pegar o menor e o maior nivel de cinza

    for i in range (256):  # Saber que é o maior e o menor nivel de cinza da imagem
        
        if( qtdNiveCinza_Pixel[i] != 0):
            MaiorNivelCinza = i

        if(qtdNiveCinza_Pixel[i] != 0 and pegueiMenorNivel == False):
            menorNivelCinza = i     
            pegueiMenorNivel = True

    limiarAnterior = (MaiorNivelCinza + menorNivelCinza) / 2   # Primeiro valor de T
    while ( (limiarAtual - limiarAnterior ) != 0 ):
    
        if (qtdInteracao == 0):                    # Primeiro interacao o valor que será colocado na "segmentacao da imagem"
            limiarAtual = limiarAnterior

        for i in range(height):  # Percorrer a Matriz linha por linha para ver que esta acima do limiar ou abaixo do limiar
            
            for j in range(width):
                   

                if(img[i][j] <= limiarAtual): # GRUPO MENOR QUE O LIMIAR

                    qtdMenorT = qtdMenorT + 1
                    somaNivelDeCinzaMenor = somaNivelDeCinzaMenor +img[i][j]
                
                elif(img[i][j] > limiarAtual): # GRUPO MAIOR QUE LIMIAR

                    qtdMaiorT = qtdMaiorT + 1
                    somaNivelDeCinzaMaior = somaNivelDeCinzaMaior + img[i][j]


        mediaMaior = somaNivelDeCinzaMaior / qtdMaiorT
   
        mediaMenor = somaNivelDeCinzaMenor / qtdMenorT 

        limiarAnterior = limiarAtual

        limiarAtual = (mediaMaior + mediaMenor)/2

        # Resetar os valores utilizados no calculo da media dos grupos para a proxima iteração

        somaNivelDeCinzaMenor = 0  
        somaNivelDeCinzaMaior = 0
        qtdMaiorT = 0
        qtdMenorT = 0
        #----------------------------

        qtdInteracao = 1
        #---------------------------------------FIM DO WHILE-----------------------------------------------

    dst = cv.threshold(img, limiarAtual, max_binary_value, 0)
    cv.imwrite("./images/edited.jpg" ,dst[1]) # Salva a imagem que voce tirou o print
    return "./images/edited.jpg"