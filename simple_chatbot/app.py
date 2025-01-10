import streamlit as st
import requests
st.title("Simple Chatbot")

# chat input, press it to /chat and get the response

user_input = st.text_input("Ask your question:")

if st.button("Send"):
    response = requests.post("http://localhost:8000/chat", json={"message": user_input})
    st.text_area("Chatbot Response:", value=response.json()["response"], height=200)



