import streamlit as st

st.title("Simple web app")


textInput = st.text_input("Enter some text", "…")

if(st.button("Start")):
    nickname = textInput.title()
    st.text("You entered: "+textInput)
