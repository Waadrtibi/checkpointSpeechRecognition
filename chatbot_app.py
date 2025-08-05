import streamlit as st
import os
import nltk
import speech_recognition as sr

nltk.download('punkt', quiet=True)

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

# Transcrire la parole en texte
def transcribe_speech():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        st.info("🎤 Parlez maintenant...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language="fr-FR")
        return text
    except sr.UnknownValueError:
        return "Je n'ai pas compris le message vocal."
    except sr.RequestError:
        return "Erreur du service de reconnaissance vocale."

def main():
    st.title("💬 Chatbot avec reconnaissance vocale")
    st.write("Posez une question en texte ou utilisez la reconnaissance vocale.")

    data_path = os.path.join(os.path.dirname(__file__), "train.txt")
    data = load_data(data_path)

    mode = st.radio("Choisissez le mode d'entrée :", ["Texte", "Voix"])

    if mode == "Texte":
        user_input = st.text_input("Entrez votre message :")
        if st.button("Envoyer"):
            if user_input:
                response = chatbot_response(user_input, data)
                st.text_area("Réponse du bot :", value=response, height=100)
    else:
        if st.button("Parler"):
            user_input = transcribe_speech()
            st.write(f"Vous avez dit : {user_input}")
            if user_input and "Je n'ai pas compris" not in user_input:
                response = chatbot_response(user_input, data)
                st.text_area("Réponse du bot :", value=response, height=100)

if __name__ == "__main__":
    main()
