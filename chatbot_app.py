import streamlit as st
import nltk
nltk.download('punkt')

# Charger les données
def load_data(filepath):
    pairs = {}
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            if ':' in line:
                question, answer = line.strip().split(':', 1)
                pairs[question.lower()] = answer
    return pairs

# Réponse du bot
def chatbot_response(user_input, data):
    user_input = user_input.lower()
    for question in data:
        if question in user_input:
            return data[question]
    return "Sorry, I didn't understand that."

# Interface Streamlit
def main():
    st.title("💬 Chatbot simple")
    st.write("Posez une question en texte et recevez une réponse instantanée.")
    
    data = load_data("C:/Users/Waad RTIBI/CheckPoint_SR/train.txt")


    user_input = st.text_input("Entrez votre message :")
    if st.button("Envoyer"):
        if user_input:
            response = chatbot_response(user_input, data)
            st.text_area("Réponse du bot :", value=response, height=100)

if __name__ == "__main__":
    main()
