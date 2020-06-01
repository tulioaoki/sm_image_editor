import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True): #pra sempre
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Muda a cor do video para cinza

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):

        dimensions = frame.shape
 
        # height, width, number of channels in image
        height = frame.shape[0]
        width = frame.shape[1]
        channels = frame.shape[2]
 
        print('Image Dimension    : ',dimensions)
        print('Image Height       : ',height)
        print('Image Width        : ',width)
        print('Number of Channels : ',channels)
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,'Nice Lucas',(30, 50), font, 2,(255,0,0),2,cv2.LINE_AA)
                    # Imagem src, Img Name, Position(x,y), Fontfamily, FontSize, color, widthFont, Default (deixa como esta) 
        cv2.imwrite("Imagem.jpeg", frame)
        break
        
# When everything done, release the capture

cap.release()
cv2.destroyAllWindows()


