from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate,load_prompt
import streamlit as st
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
st.header("Research Tool")

if not api_key:
    st.error("GEMINI_API_KEY missing in environment")
else:
    model = ChatGoogleGenerativeAI(api_key=api_key, model="gemini-2.5-flash")

    paper_input = st.selectbox("Select Research Paper Name", [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ])
    style_input = st.selectbox("Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"])
    length_input = st.selectbox("Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"])


    template=load_prompt("template.json")
   
    if st.button("Summarize"):
        chain=template | model
        result=chain.invoke({'paper_input': paper_input, 'style_input': style_input, 'length_input': length_input})
        st.write(result.content)
       
