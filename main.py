import cv2
import streamlit as st
from datetime import datetime

st.title("Motion Detector")
col1, col2 = st.columns(2)
with col1:
    start = st.button('Start Camera')
with col2:
    close = st.button('Close Camera')
if start:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)
    if close:
        camera.release()
    while True:
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Get current time as a datetime object
        now = datetime.now()

        # Get day and time add them to the frame
        cv2.putText(img=frame, text=now.strftime("%A"), org=(30, 80),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=3, color=(255, 255, 255),
                    thickness=2, lineType=cv2.LINE_AA)
        cv2.putText(img=frame, text=now.strftime("%H:%M:%S"), org=(30, 140),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=3, color=(255, 0, 0),
                    thickness=2, lineType=cv2.LINE_AA)
        streamlit_image.image(frame)