import streamlit as st
import time

# Page title
st.title('Baby Login Form')

# Guardian details
st.subheader('Guardian Information')
guardian_name = st.text_input('Guardian Name')
relationship = st.radio('Relationship with Baby', ['MOM', 'DAD', 'UNCLE', 'AUNTY', 'OTHERS'])
email = st.text_input('Email Address')

# Email validation
if email and '@' not in email:
    st.error("Please enter a valid email address.")

st.divider()

# Baby details
st.subheader('Baby Information')
baby_name = st.text_input('Baby Name')
gender = st.radio('Pick The Baby\'s Gender', ['Male', 'Female'])
dob = st.date_input('Baby\'s Date of Birth')  # Date of Birth input
age = st.slider('Baby Age (in Months)', 0, 48)

# Religion selection
religion = st.selectbox('Religion', ['Islam', 'Christianity', 'Hinduism', 'Buddhism', 'Others'])

# Form submission
if st.button('Submit'):
    # Simple validation
    if not guardian_name or not email or not baby_name:
        st.warning('Please fill in all required fields.')
    else:
        with st.spinner('Submitting...'):
            time.sleep(2)  # Simulate a delay for submission
        st.success(f'Form submitted successfully! \n Welcome {baby_name}!')
        st.balloons()

        # Optionally display submitted information
        st.write("### Submission Details")
        st.write(f"Guardian Name: {guardian_name}")
        st.write(f"Relationship with Baby: {relationship}")
        st.write(f"Email: {email}")
        st.write(f"Baby Name: {baby_name}")
        st.write(f"Gender: {gender}")
        st.write(f"Religion: {religion}")
        st.write(f"Date of Birth: {dob}")
        st.write(f"Age: {age} months")