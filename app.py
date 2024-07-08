import streamlit as st
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

GOOGLE_API_KEY = 'AIzaSyD-YUzWVLtfizySmOjwXcTMpa8ZidgqqBY';

##########################################################
genai.configure(api_key=GOOGLE_API_KEY)

# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)

model = genai.GenerativeModel('gemini-1.0-pro')

def consulta(context,prompt):
  response = model.generate_content(context + prompt)
  archivo = response.text
  with open("archivo.txt", "w") as f:
    f.write(archivo)

  return response.text

# def to_markdown(text):
#   text = text.replace('•', '  *')
#   return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

################################################################################################
# Título de la aplicación
st.title("Consultorio online")

# Texto de introducción
st.write("Bienvenido a tu consultorio online. Aqui vas a recibir una respuesta a tus dudas, estados de animo y una palabra de aliento para tu día a día y que sigas tu vida a full.")

# Entrada del prompt del usuario
prompt = st.text_area("Escribe tu estado de ánimo en una sola palabra aquí: ")

context= "Eres un especialista analizando personas. Quiero que te comportes como un anlista de estados de ánimo, y que puedas dar un consejo que pueda dar calma, ánimo, fuerza o consuelo, según corresponda. El estado de sensación que quiero que analices es: "

# Botón para mostrar el nombre
if st.button("analiza"):
    if prompt:
        # Llamar a la API y obtener la respuesta
        response = consulta(context,prompt)
        
        # Visualizar la respuesta
        st.write(response)
       
    else:
        st.write("Por favor, escribe un prompt.")