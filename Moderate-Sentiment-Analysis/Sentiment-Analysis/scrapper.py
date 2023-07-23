import requests
from bs4 import BeautifulSoup
from sentiment import calculatesentiment

def extract_text_from_link(webpage_url):
    response = requests.get(webpage_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract text from all paragraphs on the page (adjust as needed)
        paragraphs = soup.find_all('p')
        extracted_text = "\n".join(p.get_text() for p in paragraphs)
        return extracted_text
    else:
        print(f"Error: Unable to fetch content from {webpage_url}")
        return None

if __name__ == "__main__":
    # # Replace 'your_webpage_url' with the URL of the webpage you want to extract text from
    # webpage_url = 'https://www.linkedin.com/feed/update/urn:li:activity:7074101738303090688?updateEntityUrn=urn%3Ali%3Afs_feedUpdate%3A%28V2%2Curn%3Ali%3Aactivity%3A7074101738303090688%29'

    # # Extract text from the webpage
    # extracted_text = extract_text_from_link(webpage_url)

    # if extracted_text:
    #     print("Extracted Text:")
    #     print(extracted_text)

        

    

    import streamlit as st
    import sentiment

    st.title("Sentimental Analysis")
    temp="""
        <div style="background-color:tomato; padding:10px">
        <h2 style="color:white; text-align:center">Real Time Sentiment Analysis</h2>
        </div>
    """

    st.markdown(temp,unsafe_allow_html=True)
    text=st.text_input("Capition","")
    if st.button("Predict"):

        result = sentiment.calculatesentiment(text)

        st.bar_chart(data=result)

        # Get the sentiment with the highest probability
        max_sentiment = max(result, key=result.get)

        # Define button color based on the sentiment with the highest probability
        button_color = None
        if max_sentiment == 'positive':
            button_color = 'lightgreen'
        elif max_sentiment == 'neutral':
            button_color = 'yellow'
        elif max_sentiment == 'negative':
            button_color = 'tomato'

        # Apply custom CSS to style the button's background color
        button_style = f"background-color: {button_color}; padding: 0.5rem 1rem; color: black; border-radius: 0.3rem;"
        st.markdown(f'<button style="{button_style}">{max_sentiment.capitalize()} Sentiment</button>', unsafe_allow_html=True)

