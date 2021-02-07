import gc
gc.collect()

import streamlit as st
import cv2 as cv2
import numpy as np
import time

st.title('Como ficar invisível')

st.write("""
### 1) Aponte a câmera para um lugar sem movimento; 

### 2) Não fique em frente da câmera; 

### 3) Mantenha a câmera fixa; 

### 4) Quando a imagem aparecer, vista um manto vermelho e vá para frente da câmera.
""")

run = st.checkbox("Clique aqui para ligar a câmera")

cap = cv2.VideoCapture(0)
time.sleep(3)
background=0

for i in range(30):
    ret,background = cap.read()

background = np.flip(background,axis=1)

while run:
    ret, img = cap.read()

    # Inverte a imagem 
    img = np.flip(img, axis = 1)

    # Converte a imagem para o sistema de cor HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    blurred = cv2.GaussianBlur(hsv, (35, 35), 0)

    # Define a faixa inferior para detecção de cor vermelha
    lower = np.array([0,120,70])
    upper = np.array([10,255,255])
    mask1 = cv2.inRange(hsv, lower, upper)

    # Define a faixa superior para detecção de cor vermelha
    lower_red = np.array([170,120,70])
    upper_red = np.array([180,255,255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    # Une as duas máscaras para gerar a máscara final
    mask = mask1 + mask2
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5,5), np.uint8))

    # Troca os pixels da capa vermelha capturada pela câmera pelos pixels da foto inicial
    img[np.where(mask == 255)] = background[np.where(mask == 255)]
    cv2.imshow('Display',img)
    k = cv2.waitKey(10)
    if k == 27:
        break
