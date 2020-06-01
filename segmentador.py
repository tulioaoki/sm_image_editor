import cv2


def segmentar(image):
    img = cv2.imread(image)
    if img is None:
        raise Exception("Erro ao abrir imagem" + str(image))
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    h = img.shape[0]
    w = img.shape[1]
    max_binary_value = 255
    qtd_pixel = h * w
    menor_t = 0
    maior_t = 1
    media_maior = 0
    media_menor = 0
    menor_n_cinza = 0
    maior_n_cinza = 0
    menor_loop = False
    dst = None
    sum_ncmaior = 0
    sum_ncmenor = 0
    prev_l = None
    l_now = 255
    qtd_n_cinza_pixel = [0]*256
    qint = 0

    for x in range(h):
        for y in range(w):
            gray_level = img[x][y]
            prev_qtd = qtd_n_cinza_pixel[gray_level]
            sum = prev_qtd + 1
            qtd_n_cinza_pixel[gray_level] = sum

    for i in range(256):
        if qtd_n_cinza_pixel[i] != 0:
            maior_n_cinza = i
        if qtd_n_cinza_pixel[i] != 0 and not menor_loop:
            menor_n_cinza = i
            menor_loop = False

    prev_l = (maior_n_cinza+menor_n_cinza)/2
    print("Carregando...")
    while (l_now - prev_l) != 0:
        if qint == 0:
            l_now = prev_l

        for x in range(h):
            for y in range(w):
                if img[x][y] <= l_now:
                    menor_t = menor_t + 1
                    sum_ncmenor = sum_ncmenor + img[x][y]
                elif img[x][y] > l_now:
                    maior_t = maior_t + 1
                    sum_ncmaior = sum_ncmaior + img[x][y]

        media_maior = sum_ncmaior/maior_t
        media_menor = sum_ncmenor/menor_t

        prev_l = l_now
        l_now = (media_maior+media_menor)/2

        sum_ncmenor = 0
        sum_ncmaior = 0
        menor_t = 0
        maior_t = 0
        qint = 1

    dst = cv2.threshold(img, l_now, max_binary_value,0)
    name = image.split(".")[0]
    final = "{}_segmentada.jpg".format(name)
    cv2.imwrite(final, dst[1])
    return final
