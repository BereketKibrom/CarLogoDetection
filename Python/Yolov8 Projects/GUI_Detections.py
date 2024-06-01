import cv2
import streamlit as st
from PIL import Image
from ultralytics import YOLO
import numpy as np
import time

# Load the YOLOv8 model
model = YOLO('best1.pt')

# Initialize Streamlit
st.title("Car Logo Detection")
st.sidebar.title("Options")

# Initialize session state for selectbox control
if 'selectbox_disabled' not in st.session_state:
    st.session_state.selectbox_disabled = False

# Create a disabled selectbox if the condition is met
if st.session_state.selectbox_disabled:
    option = st.sidebar.selectbox(
        'Choose the mode',
        ('Load Image and Predict', 'Start Live Stream Detection'),
        disabled=True
    )
else:
    option = st.sidebar.selectbox(
        'Choose the mode',
        ('Load Image and Predict', 'Start Live Stream Detection')
    )

# Function to process and display image
def process_and_display_image(image):
    results = model(image)
    annotated_image = results[0].plot()
    img_rgb = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
    return img_rgb

# Image mode
if option == 'Load Image and Predict':
    uploaded_file = st.sidebar.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        st.write("")
        st.write("Detecting objects...")
        annotated_image = process_and_display_image(image)
        st.image(annotated_image, caption='Detected Image', use_column_width=True)

# Live stream mode
elif option == 'Start Live Stream Detection':
    if st.sidebar.button("Start Live Stream"):
        st.session_state.selectbox_disabled = True
        st.session_state.live_stream_active = True

    if 'live_stream_active' not in st.session_state:
        st.session_state.live_stream_active = False

    if st.session_state.live_stream_active:
        cap = cv2.VideoCapture(1)  # Use 0 for webcam
        stframe = st.empty()
        stop_button = st.sidebar.button("Stop Live Stream")

        # Set the frame rate
        FRAME_RATE = 1/20  # 30 FPS

        while st.session_state.live_stream_active:
            start_time = time.time()

            ret, frame = cap.read()
            if not ret:
                st.write("Failed to capture image")
                break

            annotated_frame = process_and_display_image(frame)
            stframe.image(annotated_frame, channels="RGB")

            # Control the frame rate
            elapsed_time = time.time() - start_time
            time.sleep(max(0, FRAME_RATE - elapsed_time))

            # Check for stop button click
            if stop_button:
                st.session_state.live_stream_active = False
                st.session_state.selectbox_disabled = False

        cap.release()
        st.write("Live stream stopped.")
