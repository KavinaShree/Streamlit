import os
import streamlit as st
from PIL import Image as PILImage

# Title of the app
st.title("Parenting Tips")

# Ask for the number of months pregnant
months_pregnant = st.number_input("How many months are you pregnant?", min_value=0, max_value=9, step=1)

# Recommendations based on the number of months pregnant
recommendations = {
    1: ["Prenatal vitamins", "First prenatal visit", "Pregnancy journal"],
    2: ["Choose a healthcare provider", "Discuss birth plan", "Baby names"],
    3: ["Maternity clothes", "Childbirth classes", "Prepare home for baby"],
    4: ["Crib or bassinet", "Baby registry", "Baby clothes"],
    5: ["Feeding supplies (bottles, bibs)", "Baby shower planning", "Research pediatricians"],
    6: ["Stroller", "Car seat", "Diapers and wipes"],
    7: ["Pack hospital bag", "Finish baby registry", "Baby-proofing supplies"],
    8: ["Install car seat", "Arrange help after birth", "Tour birthing facility"],
    9: ["Prepare for labor", "Check essentials", "Enjoy final days"]
}

# Generate the recommendations based on the pregnancy month
if months_pregnant > 0:
    st.header("Recommendations Based on Your Pregnancy Month")
    st.write("Here are some things you should consider buying:")
    for item in recommendations[months_pregnant]:
        st.write(f"- {item}")

st.divider()
# Input text or image section
st.header("Check list or Picture of the bought stuff for Baby")
st.write("Please let us know if you have prepared everything adequately!")

# Text input for user feedback
user_input = st.text_area("What else do you think should be prepared?", height=150)

# Image upload for user to share pictures
uploaded_image = st.file_uploader("Upload a picture of your preparations", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    # Display the uploaded image
    img = PILImage.open(uploaded_image)
    st.image(img, caption="Uploaded Image of Preparations", use_column_width=True)

    # Here you would implement an image recognition function.
    # For now, we will simulate the result.
    recognized_items = ["Crib", "Baby clothes", "Diapers"]  # Mockup list of recognized items
    st.write("The following items have been recognized in your image:")
    for item in recognized_items:
        st.write(f"- {item}")

# Display the user's text input
if user_input:
    st.write("You mentioned:")
    st.write(user_input)
    
st.divider()
# Ask if the user needs exercise recommendations
st.header("Do you need any exercise recommendations for yourself as a mom?")
exercise_needed = st.radio("", ("Yes", "No"))  # No label for the radio buttons

# Provide exercise recommendations based on pregnancy month if they say yes
if exercise_needed == "Yes":
    st.header("Exercise Recommendations")

    exercises = {
        1: ["Walking", "Gentle stretching", "Pelvic tilts"],
        2: ["Walking", "Prenatal yoga", "Swimming"],
        3: ["Walking", "Low-impact aerobics", "Bodyweight exercises"],
        4: ["Walking", "Pregnancy yoga", "Kegel exercises"],
        5: ["Walking", "Pilates for pregnancy", "Light resistance training"],
        6: ["Walking", "Water aerobics", "Stretching"],
        7: ["Walking", "Prenatal dance", "Gentle strength training"],
        8: ["Walking", "Breathing exercises", "Pelvic floor exercises"],
        9: ["Gentle walking", "Relaxation exercises", "Preparation for labor exercises"]
    }

    if months_pregnant in exercises:
        st.header("Here are some exercises you can do this month:")
        for exercise in exercises[months_pregnant]:
            st.write(f"- {exercise}")
