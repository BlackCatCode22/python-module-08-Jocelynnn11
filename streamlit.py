import streamlit as st
import openai
import os
from dotenv import load_dotenv
from apikey import apikey

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY") or apikey  # Using .env or fallback to apikey.py

def main():
    # Initialize Streamlit application
    st.set_page_config(page_title="Recipe Suggester Chatbot", page_icon="🍳", layout="wide")

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
                st.write(":green[_Your question_:]", user_input)  # Display user input

        with right_column:
            with st.chat_message("assistant"):
                try:
                    if user_input:
                        # Make the API call to OpenAI
                        completion = openai.ChatCompletion.create(
                            model="gpt-3.5-turbo",
                            messages=[
                                {"role": "system",
                                 "content": "You are a wonderful assistant for aspiring chefs named Bella, and you help them find delicious recipes, suggest creative meal ideas, and guide them through cooking step-by-step. You are knowledgeable about various cuisines, dietary restrictions, and cooking techniques. Your goal is to make cooking enjoyable and accessible for everyone."},
                                {"role": "user", "content": user_input}
                            ]
                        )

                        # Get the response from the API
                        answer = completion['choices'][0]['message']['content']
                        st.write("🤖 :red[_Chatbot Response_:]", answer)

                except Exception as e:
                    st.write("🤖 :red[Chatbot Response:]", e)
                    st.write("I'm sorry, I couldn't generate a response.")

if __name__ == "__main__":
    main()

