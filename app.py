import google.generativeai as genai
import streamlit as st
from PIL import Image
Google_Api_key=""
genai.configure(api_key=Google_Api_key)
model=genai.GenerativeModel("gemini-pro-vision")

def get_response(input,image,prompt):
    response=model.generate_content([input,image[0],prompt])
    return response.text

def get_image_detail(uploaded_image):
    if uploaded_image is not None:
        byte_data=uploaded_image.getvalue()
        image_details=[
            {
                "mime_type":uploaded_image.type,
                "data":byte_data
            }
        ]
        return image_details
    else:
        raise FileNotFoundError("No file Uploaded")

st.set_page_config(page_title="Multilanguage Invioce Extractor")
st.header("Multilanguage Invioce Extractor")
input=st.text_input("Input prompt:",key="input")
uploaded_image=st.file_uploader("Upload the image of your invoice",type=["jpg","jpeg","png"])
image=""
if uploaded_image is not None:
    image=Image.open(uploaded_image)
    st.image(image,caption="uploaded image.")

submit=st.button("Tell me about the invoice")
input_prompt="""You are an expect in understanding invoices. We will upload an image as invoice 
and you will have to answer any questions based on the uploaded invoice image"""
if submit:
    input_data=get_image_detail(uploaded_image)
    response=get_response(input_prompt,input_data,input)
    st.subheader("The Response is:")
    st.write(response)
