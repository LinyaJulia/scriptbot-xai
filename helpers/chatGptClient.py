from openai import OpenAI
import streamlit as st

class ChatGPTClient(): 
    apikey = st.secrets["apikey"]
    client = ""

    def __init__(self):
        self.client = OpenAI(api_key=self.apikey)

    def chat(self, messages):
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            temperature=1,
            max_tokens=1500,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )

        return response.choices[0].message.content
