import streamlit as st
import sentiment

st.title("Sentimental Analysis")
temp="""
    <div style="background-color:tomato; padding:10px">
    <h2 style="color:white; text-align:center">Real Time Sentiment Analysis</h2>
    </div>
"""

st.markdown(temp,unsafe_allow_html=True)
text=st.text_input("Text","")
if st.button("Predict"):
    print(text)
    result=sentiment.calculatesentiment(text)
    st.success(result)
