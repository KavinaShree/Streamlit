import streamlit as st

#Set the app title
st.title('My first streamlit app')

#streamlit run [file name].py
#Display text output
st.write('welcome to my first streamlit app')

#Display a button
st.button("Reset", type="primary")
if st.button("Say Hello"):
  st.write("Why hello there")
else:
  st.write("Goodbye")
