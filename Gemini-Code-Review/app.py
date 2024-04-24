import google.generativeai as genai
import streamlit as st

f=open("keys/.gemini.txt")
key=f.read()
genai.configure(api_key=key)

# Set colored page title
st.markdown("<h1 style='color:pink;'>Python Code Review with GeminiAI</h1>", unsafe_allow_html=True)

# User input section
st.markdown("<h2 style='color:green;'>Enter Your Python Code</h2>", unsafe_allow_html=True)
prompt = st.text_area("Enter your Python code here:", height=200)

# Button to trigger code review
if st.button("Review the Code"):
    st.markdown("<h2 style='color:blue;'>Review Result</h2>", unsafe_allow_html=True)

    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                  system_instruction="""Review the given python code and Generate what are the list of mistakes in the code and give fixed code by correcting the code""")
    

    
    response = model.generate_content(prompt)
    st.write(response.text)