import cv2
webcam = cv2.VideoCapture(0)
while True:
    sucesso, imagem = webcam.read()
    cv2.imshow('projeto 4 - ia', imagem)
    if cv2.waitKey(1) !=-1:
        break
webcam.release()
cv2.destroyAllWindows()

