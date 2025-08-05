import streamlit as st
import nltk
import os

nltk.download('punkt', quiet=True)

# Charger les données avec chemin relatif
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
    
    # Chemin relatif au fichier train.txt dans le même dossier que ce script
    data_path = os.path.join(os.path.dirname(__file__), "train.txt")
    data = load_data(data_path)

    user_input = st.text_input("Entrez votre message :")
    if st.button("Envoyer"):
        if user_input:
            response = chatbot_response(user_input, data)
            st.text_area("Réponse du bot :", value=response, height=100)

if __name__ == "__main__":
    main()
