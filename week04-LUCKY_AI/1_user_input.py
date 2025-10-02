import streamlit as st

if prompt := st.chat_input("What is your name?"):

    st.chat_message("user").write(prompt)