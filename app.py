import streamlit as st
import pickle   
import json
import random #random module is used to select any radnom number or choice from a list or range of numbers

st.title("Simple ChatBot")

try:
    #load dataset
    with open('intents.json') as file:
        data = json.load(file)
    #load model and vectorizer
    model = pickle.load(open('chatbot_model.pkl', 'rb'))
    vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

except Exception as e:
    st.error(f"Error loading model files: {e}")
    st.stop()

def chatbot_response(user_input):
    input_vec = vectorizer.transform([user_input.lower()])
    tag = model.predict(input_vec)[0]
    
    for intent in data['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])
    
if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("You: ")

if user_input:
    respomse = chatbot_response(user_input)
    st.session_state.messages.append(("You", user_input))
    st.session_state.messages.append(("Bot", respomse))




for sender, msg in st.session_state.messages:
    if sender == "You":
        st.write("You:",msg)
    else:
        st.write("Bot:",msg)