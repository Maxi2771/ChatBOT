import streamlit as st
import os
from groq import Groq

print("Astrid en línea")

api_groc = st.secrets.get("clave_api")

cliente = Groq(api_key=api_groc)

st.set_page_config(page_title="Astrid Bot", page_icon="https://i.pinimg.com/736x/d9/1a/bd/d91abd84ccc65728572a5d82e565bb69.jpg", layout="centered")
st.title('''Hola soy :violet[Astrid]''')
st.header("Soy una IA diseñada para ayudarte a resolver tus dudas.")

if "usuario" not in st.session_state:
    st.session_state.usuario = ""
if "logueado" not in st.session_state:
    st.session_state.logueado = False
if "mensajes" not in st.session_state:
    st.session_state.mensajes = [
        {"role": "system", "content": "Eres una asistente amigable llamada Astrid."}
    ]

if not st.session_state.logueado:
    nombre = st.text_input("¿Cómo te llamas?")
    if st.button("Ingresar"):
        if nombre.strip():
            st.session_state.usuario = nombre.strip()
            st.session_state.logueado = True
            st.success(f"¡Bienvenido {nombre}!")
        else:
            st.warning("Por favor, ingresa tu nombre.")
else:
    st.subheader(f"Hola {st.session_state.usuario}, ¿qué quieres preguntarme?")


modelos = ['llama3-8b-8192', 'llama3-70b-8192', 'gemma2-9b-it', 'whisper-large-v3']
modelo_seleccionado = st.selectbox("Selecciona un modelo", modelos)

pregunta = st.text_input("Escribe tu pregunta aquí", key="input_pregunta")

if st.button("Preguntar"):
        if pregunta.strip():
            st.session_state.mensajes.append({"role": "user", "content": pregunta.strip()})
            
            with st.spinner("Astrid está pensando..."):
                respuesta = cliente.chat.completions.create(
                    model=modelo_seleccionado,
                    messages=st.session_state.mensajes
                )
                contenido_respuesta = respuesta.choices[0].message.content
                st.session_state.mensajes.append({"role": "assistant", "content": contenido_respuesta})
                st.success("Astrid responde:")
                st.markdown(contenido_respuesta)
        else:
            st.warning("Escribe algo para preguntar.")

with st.expander("📝 Historial de conversación"):
        for msg in st.session_state.mensajes[1:]: 
            if msg["role"] == "user":
                st.markdown(f"**🧑 {st.session_state.usuario}:** {msg['content']}")
            elif msg["role"] == "assistant":
                st.markdown(f"**🤖 Astrid:** {msg['content']}")