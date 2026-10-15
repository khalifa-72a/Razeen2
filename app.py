import streamlit as st
from google import genai

st.title("My Smart App 🤖")

api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.warning("Please add your API key in the app secrets.")
else:
    client = genai.Client(api_key=api_key)
    user_input = st.text_input("Type your message here:")

    if st.button("Send") and user_input:
        with st.spinner("Thinking..."):
            response = client.models.generate_content(
                model="gemini-1.5-flash",
                contents=user_input,
            )
            st.write(response.text)
