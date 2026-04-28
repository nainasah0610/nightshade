import streamlit as st 
#Title of App
st.title("My first streamlit app")
#adding text
st.write("Hello! Creating a simple web application using streamlit library")

#Text input:
name= st.text_input("Enter your name: ")
#Number input:
age=st.number_input("Enter your age: ")

#Display a message when the button is clicked:
if st.button("Submit"):
  st.write("Hello,{name}!Welcome to steamlit.")
