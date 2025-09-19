import os
import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="OpenAI test", page_icon="🤖")

api_key = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")

def mask(k):
    if not k: return "None"
    return f"{k[:7]}...{k[-4:]} (len={len(k)})"

st.text(f"Key detected: {mask(api_key)}")  # Remove after verifying

if not api_key:
    st.error("Missing OPENAI_API_KEY. Add it in Streamlit Secrets.")
    st.stop()

client = OpenAI(api_key=api_key)

st.title("OpenAI API quick test")
prompt = st.text_input("Ask anything:", "Say hi in one short sentence.")
if st.button("Run"):
    try:
        with st.spinner("Contacting OpenAI..."):
            resp = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=50,
            )
        st.write(resp.choices[0].message.content)
    except Exception as e:
        st.error(str(e))
