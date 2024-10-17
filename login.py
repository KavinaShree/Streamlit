import streamlit as st
from datetime import datetime

# Initialize session state for storing user data
if 'user_data' not in st.session_state:
    st.session_state.user_data = {}

def calculate_age_in_months(dob):
    """Calculate age in months based on the date of birth."""
    today = datetime.today()
    age_in_months = (today.year - dob.year) * 12 + today.month - dob.month
    return age_in_months

def sign_up():
    st.header("Sign Up")
    guardian_name = st.text_input("Guardian Name")
    relationship = st.selectbox("Relationship with Baby", ["Mom", "Dad", "Uncle", "Aunty", "Others"])
    email = st.text_input("Email Address")

    # Baby Information
    st.subheader("Baby Information")
    baby_name = st.text_input("Baby Name")
    baby_gender = st.selectbox("Baby Gender", ["Male", "Female", "Other"])
    date_of_birth = st.date_input("Date of Birth")

    if st.button("Sign Up"):
        # Check if email already exists
        if email in st.session_state.user_data:
            st.error("Email already registered. Please log in.")
        else:
            # Calculate age in months
            age_in_months = calculate_age_in_months(date_of_birth)

            # Store user data in the session state dictionary
            st.session_state.user_data[email] = {
                'guardian_name': guardian_name,
                'relationship': relationship,
                'baby_name': baby_name,
                'baby_gender': baby_gender,
                'date_of_birth': date_of_birth,
                'month': date_of_birth.strftime("%B"),
                'age_in_months': age_in_months  # Store calculated age in months
            }
            st.success("Sign Up Successful! You can now log in.")
            st.balloons()  # Add balloon effect

def login():
    st.header("Login")
    email = st.text_input("Email Address")

    if st.button("Login"):
        if email in st.session_state.user_data:
            user_info = st.session_state.user_data[email]
            st.success(f"Login Successful! Welcome back, {user_info['guardian_name']}!")
            st.write(f"Baby Name: {user_info['baby_name']}")
            st.write(f"Baby Gender: {user_info['baby_gender']}")
            st.write(f"Date of Birth: {user_info['date_of_birth']}")
            st.write(f"Month: {user_info['month']}")
            st.write(f"Age: {user_info['age_in_months']} months")  # Display age in months
            st.balloons()  # Add balloon effect
        else:
            st.error("Email not found. Please sign up first.")

def main():
    st.title("Baby Care App")

    menu = ["Sign Up", "Login"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Sign Up":
        sign_up()
    elif choice == "Login":
        login()

if __name__ == "__main__":
    main()
