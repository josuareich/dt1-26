
import streamlit as st
import requests
import os

st.title("A Simple Chat System")

# Backend connection
BASE_URL = os.getenv("BASE_URL", "http://api:5001").rstrip("/")

# User input
user_input = st.text_input("Ask me something")

# OpenRouter model
model_id = "nvidia/nemotron-3-ultra-550b-a55b:free"

# Chat button
if st.button("chat"):
    if not user_input.strip():
        st.warning("Please enter a message.")
    else:
        with st.spinner(f"Calling {model_id}..."):
            try:
                response = requests.get(
                    f"{BASE_URL}/chat",
                    params={
                        "model_id": model_id,
                        "input": user_input
                    },
                    timeout=120
                )

                if response.status_code == 200:
                    st.success("Success!")
                    st.write(response.json().get("ack"))
                else:
                    st.error(
                        f"Failed: {response.status_code}"
                    )

            except requests.exceptions.RequestException as e:
                st.error(f"Connection error: {e}")
