import cv2

def takePic(nome):
    cam_port = 1 #1 para o pedro
    cam = cv2.VideoCapture(cam_port) 

    while True:
        # Captura um frame da câmera
        ret, frame = cam.read() 

        # Exibe o frame em tempo real
        cv2.imshow("Camera", frame) 

        # Aguarda a entrada do teclado por um curto período de tempo
        key = cv2.waitKey(1)

        # Se a tecla 's' for pressionada (código ASCII 115)
        if key == 115:
            # Salva o frame como imagem
            cv2.imwrite(f"images/{nome}.jpg", frame)
            print("Foto tirada!")
            break  # Sai do loop


    cv2.destroyAllWindows()

