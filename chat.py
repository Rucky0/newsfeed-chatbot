import streamlit as st
import random
import time
import requests
from url import API_GATEWAY_URL

def api_call(input):
    # Define the URL for the API endpoint
    url = API_GATEWAY_URL
    payload = {"input": input}
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # The request was successful, so we can process the response data
        data = response.json()
    else:
        print("The request was not successful")
    return data

st.title("Simple chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("How can I assist you?"):
    
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):

        api_text = api_call(prompt)['content'][0]['text']
        response = st.write(api_text)#APICALL


        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": api_text})