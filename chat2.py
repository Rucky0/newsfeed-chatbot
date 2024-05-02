import streamlit as st
import requests  # Import the requests library to make HTTP requests

st.title("Chatbot Interface")

# Assuming you have stored your API's URL and endpoint in Streamlit's secrets
api_url = st.secrets["API_URL"]

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Construct the payload to send to your chatbot backend
    payload = {
        "model": "your_model_identifier",  # Adjust this as necessary for your backend
        "messages": [
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages
        ]
    }

    # Make the HTTP request to your backend
    response = requests.post(api_url, json=payload)

    if response.status_code == 200:
        chat_response = response.json().get('response', 'No response received.')
        st.session_state.messages.append({"role": "assistant", "content": chat_response})
        
        with st.chat_message("assistant"):
            st.markdown(chat_response)
    else:
        st.error("Failed to get response from the server. Please check the server logs.")
