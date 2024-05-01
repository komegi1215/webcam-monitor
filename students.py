import cv2
import streamlit as st
import datetime

st.title("Motion Detector")
start = st.button("Start Camera")

if start:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)

    while True:
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        current_datetime = datetime.datetime.now()
        day = current_datetime.strftime("%A")
        datetime_str = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

        cv2.putText(frame, f"Day: {day}", (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (20, 100, 200), 2, cv2.LINE_AA)
        cv2.putText(frame, f"Time: {datetime_str}", (50, 100), cv2.FONT_HERSHEY_PLAIN, 2, (20, 100, 200), 2,
                    cv2.LINE_AA)
        streamlit_image.image(frame)