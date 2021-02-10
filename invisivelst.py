import streamlit as st
import cv2 as cv2

st.title('Streamlit OpenCV Camera Test')

MAX_FRAMES = st.slider("Select number of frames to render:", min_value=60, max_value=600, value=300, step=30)
run = st.button("Click to render server camera")

if run:
    capture = cv2.VideoCapture(0)
    img_display = st.empty()
    for i in range(MAX_FRAMES):
        ret, img = capture.read()
        img_display.image(img, channels='BGR')
    capture.release()
    st.markdown("Render complete")
