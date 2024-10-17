import os
import streamlit as st
import cv2
import numpy as np
from PIL import Image as PILImage

# Home safety function to analyze the image for potential risks
def detect_risks(image):
    # Convert the image to grayscale for edge detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply edge detection (Canny Edge Detector)
    edges = cv2.Canny(gray, 100, 200)

    # Detect corners (representing sharp edges)
    corners = cv2.goodFeaturesToTrack(gray, 50, 0.01, 10)

    # Handle case where no corners are detected
    risks_detected = 0
    if corners is not None:
        corners = np.int64(corners)  # Ensure corners is in the correct format
        for corner in corners:
            x, y = corner.ravel()
            cv2.circle(image, (x, y), 5, (0, 0, 255), -1)  # Mark risky areas with red circles
            risks_detected += 1

    return image, risks_detected

# Function to generate safety suggestions
def safety_suggestions(risk_count):
    if risk_count > 0:
        return f"{risk_count} potential risks detected. Cover sharp edges with corner protectors and ensure hazardous areas are blocked off."
    else:
        return "No significant risks detected in this area."

# Streamlit app layout
st.title("Baby Care Assistant - Home Safety")

# File uploader for the user to upload a home picture
uploaded_file = st.file_uploader("Upload a picture of a room", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load and display the image using PIL and resize for better UI display
    img = PILImage.open(uploaded_file)
    img = img.resize((800, 600))  # Optional resizing step
    img_array = np.array(img)

    # Detect risks in the image (e.g., sharp corners)
    detected_image, risk_count = detect_risks(img_array)

    # Display the original and processed image with marked risks
    st.image(img, caption="Uploaded Image", use_column_width=True)
    st.image(detected_image, caption="Risks Detected (marked in red)", use_column_width=True)

    # Provide safety suggestions based on the number of risks detected
    suggestions = safety_suggestions(risk_count)
    st.write(suggestions)

    # Display additional general suggestions
    st.write("## General Safety Tips:")
    st.write("""
    - **Cover sharp corners**: Use corner guards for tables and furniture edges.
    - **Anchor heavy furniture**: Ensure shelves, cabinets, and other heavy items are secured to prevent tipping.
    - **Block access to hazardous areas**: Use baby gates to restrict access to stairs or dangerous rooms.
    - **Ensure outlets are covered**: Use child-proof covers for electrical outlets.
    """)

else:
    st.write("Please upload a picture of a room to analyze the safety risks.")
