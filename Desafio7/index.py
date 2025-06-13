import streamlit as st
from groq import Groq

st.set_page_config(page_title="ChatBot", page_icon="🤖")
st.title("ChatBot")

modelos = ['llama3-8b-8192', 'llama3-70b-8192', 'gemma2-9b-it']

def configurar_pagina():
    st.sidebar.title("Configurar IA")
    elegirModelo = st.sidebar.selectbox("Elegí un modelo", options=modelos, index=0)
    return elegirModelo

def crear_usuario():
    claveSecreta = st.secrets["clave_api"]
    return Groq(api_key=claveSecreta)

def configurar_modelo(cliente, modelo, promptDeEntrada):
    return cliente.chat.completions.create (
        model = modelo,
        messages = [{"role": "user", "content": promptDeEntrada}],
        stream=True
    )

def inicializar_estado():
    if "mensajes" not in st.session_state:
        st.session_state.mensajes = []

clienteUsuario = crear_usuario() 
inicializar_estado() 
modelo = configurar_pagina()

prompt = st.chat_input("Escribe aquí")

if prompt:
    configurar_modelo(clienteUsuario, modelo, prompt)
    st.write(f"Usuario: {prompt}")
    print(prompt)