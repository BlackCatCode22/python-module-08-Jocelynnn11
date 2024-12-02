import openai
import os
import streamlit as st
from dotenv import load_dotenv
from apikey import apikey

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from environment variables
apikey = os.getenv("OPENAI_API_KEY")

# Configure OpenAI API with your key
openai.api_key = apikey

def main():
    # Initialize Streamlit application
    st.set_page_config(page_title="Recipe Suggester Chatbot", page_icon="🤖", layout="wide")

    # ----HEADER SECTION----
    with st.container():
        st.header("Python Chatbot using Streamlit and OpenAI ChatGPT 3.5")
        st.title("Recipe Suggester Assistant")
        st.divider()

    # ----MAIN SECTION----
    with st.container():
        user_input = st.text_input("Ask me anything about Recipes", "")
        st.divider()

    # ----OUTPUT SECTION----
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            with st.chat_message("user"):
                st.write(":green[_Your question_:]", user_input)

        with right_column:
            with st.chat_message("assistant"):
                try:
                    if user_input:
                        # Generate response using OpenAI's GPT-3.5-turbo
                        completion = openai.ChatCompletion.create(
                            model="gpt-3.5-turbo",
                            messages=[
                                {"role": "system",
                                 "content": "You are a wonderful assistant for aspiring chefs named Bella, helping with recipe suggestions."},
                                {"role": "user", "content": user_input}
                            ]
                        )
                        answer = completion.choices[0].message['content']
                        st.write("🤖 :red[_Chatbot Response_:]", answer)

                except Exception as e:
                    st.write(f"🤖 :red[Chatbot Response Error: {e}]")

if __name__ == "__main__":
    main()
