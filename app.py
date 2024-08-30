## 1.Primero correr pip install openai y pip install streamlit en la terminal

## 2. Conectarse a la API de Chatgpt guardando este archivo

import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="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")

# Configura tu API key de OpenAI

# Título de la aplicación
st.title("Chat con nuestro chatbot DATA & INSIGHTS")

# Campo de entrada de texto
user_input = st.text_input("Escribe tu mensaje:")

# Botón para enviar el mensaje
if st.button("Enviar"):
    # Crear una solicitud de completado
    completion = client.chat.completions.create(model="gpt-4",
    messages=[
        {"role": "user", "content": user_input}
    ])

    # Mostrar la respuesta del modelo
    response = completion.choices[0].message.content
    st.write(response)


## 3. Correr  streamlit run app.py en tu terminal 