import streamlit as st
import nltk
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

# Ensure nltk punkt tokenizer is downloaded
nltk.download('punkt')

# Load the SentenceTransformer model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def load_model(model_path):
    with open(model_path, "rb") as file:
        return pickle.load(file)

def make_prediction(user_text, selected_model):
    # Process the text
    sentences = nltk.sent_tokenize(user_text)
    embeddings = [model.encode(sentence) for sentence in sentences]
    essay_embedding = sum(embeddings) / len(embeddings)
    
    # Make prediction
    prediction = selected_model.predict([essay_embedding])[0]
    
    # Convert 0s to "Não" and 1s to "Sim"
    return ['Sim' if pred == 1 else 'Não' for pred in prediction]

def main():
    st.title("Aplicação de Predição")
    
    # Model selection dropdown
    model_option = st.selectbox("Selecione o modelo de IA:", ["Modelo 1", "Modelo 2", "Modelo 3"])
    
    if model_option == "Modelo 1":
        loaded_model = load_model("C:/Users/moura/Projetos/Colab-Essays/forest-essays/random_forest_model.pkl")  # Model 1 path
    elif model_option == "Modelo 2":
        loaded_model = load_model("C:/Users/moura/Projetos/Colab-Essays/forest-mypersonality/mypersonality_forest.pkl")  # TODO: Update the path for Model 2
    else:
        loaded_model = load_model("C:/Users/moura/Projetos/Colab-Essays/LSTM-essays/model_LSTM.pkl")  # TODO: Update the path for Model 3
    
    # User input for text
    user_text = st.text_area("Por favor, insira o texto:", "")
    
    if st.button("Fazer Predição"):
        prediction = make_prediction(user_text, loaded_model)
        st.write("Resultado da Predição:")
        st.write(prediction)

if __name__ == "__main__":
    main()