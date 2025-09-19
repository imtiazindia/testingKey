# streamlit_app.py
import os
import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="OpenAI test", page_icon="🤖")

api_key = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("Missing OPENAI_API_KEY. Add it in Streamlit Secrets.")
    st.stop()

client = OpenAI(api_key=api_key)

st.title("OpenAI API quick test")
prompt = st.text_input("Ask anything:", "Say hi in one short sentence.")
if st.button("Run"):
    with st.spinner("Contacting OpenAI..."):
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100,
        )
    st.write(resp.choices[0].message.content)
