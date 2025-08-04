import streamlit as st
import speech_recognition as sr
import nltk
nltk.download('punkt')

# 🧠 Charger les données d'entraînement depuis train.txt
def load_data(filepath):
    pairs = {}
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            if ':' in line:
                question, answer = line.strip().split(':', 1)
                pairs[question.lower()] = answer
    return pairs

# 🤖 Fonction de traitement NLP simple avec correspondance mot-clé
def chatbot_response(user_input, data):
    user_input = user_input.lower()
    for question in data:
        if question in user_input:
            return data[question]
    return "Sorry, I didn't understand that."

# 🎙️ Reconnaissance vocale avec microphone
def transcribe_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎤 Speak now...")
        audio = r.listen(source, timeout=5)
    try:
        text = r.recognize_google(audio)
        st.success(f"🗣️ You said: {text}")
        return text
    except sr.UnknownValueError:
        st.warning("❌ Speech not understood.")
        return ""
    except sr.RequestError:
        st.error("⚠️ Speech Recognition API unavailable.")
        return ""

# 🚀 Interface Streamlit
def main():
    st.title("🎙️ Chatbot vocal et texte avec Python")
    st.write("Interagissez avec le chatbot par texte ou par voix.")

    # Charger le fichier d'entraînement
    data = load_data("C:/Users/Waad RTIBI/CheckPoint_SR/train.txt")


    input_mode = st.radio("Choisissez un mode d'entrée :", ["Texte", "Voix"])

    if input_mode == "Texte":
        user_input = st.text_input("Tapez votre message :")
        if st.button("Envoyer"):
            if user_input:
                response = chatbot_response(user_input, data)
                st.text_area("Réponse du chatbot :", value=response, height=100)
    else:
        if st.button("🎤 Parler"):
            speech_text = transcribe_speech()
            if speech_text:
                response = chatbot_response(speech_text, data)
                st.text_area("Réponse du chatbot :", value=response, height=100)

if __name__ == "__main__":
    main()
