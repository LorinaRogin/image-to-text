import requests
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-base"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

output = query("plant 4.jpg")

st.file_uploader("upload an image", type="jpg")
if st.button('Click me!'):
    st.write(output)