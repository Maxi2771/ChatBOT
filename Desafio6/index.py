import streamlit as st
st.set_page_config(page_title="Astrid Bot", page_icon="https://i.pinimg.com/736x/d9/1a/bd/d91abd84ccc65728572a5d82e565bb69.jpg", layout="centered")
st.title('''Hola soy :red[Astrid]''')
st.header("Soy una IA diseñada para ayudarte a resolver tus dudas.")
nombre = st.text_input("¿Cómo te llamas?")
if st.button(''':blue[Enviar]'''):
    if nombre:
        st.info(f"Bienvenido :blue[{nombre}], soy :red[Astrid]!")
        st.image("https://i.pinimg.com/736x/86/4a/f6/864af61a12e4b018182217c55d146b21.jpg", width=300)
    else:
        st.error("Por favor, ingresa tu nombre.")
        st.image("https://i.pinimg.com/736x/10/7a/a9/107aa9560c59a0f8a1f0a82005aecea9.jpg", width=300)