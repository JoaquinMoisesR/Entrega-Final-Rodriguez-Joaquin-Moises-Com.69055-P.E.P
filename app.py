import streamlit as st
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# API KEY de Google AI Studio - Gemini

GOOGLE_API_KEY = 'AIzaSyD-YUzWVLtfizySmOjwXcTMpa8ZidgqqBY';

genai.configure(api_key=GOOGLE_API_KEY)

# Modelo de generación de contenido con Gemini AI Studio - 'gemini-1.0-pro'
model = genai.GenerativeModel('gemini-1.0-pro')

def consulta(context,prompt):
  response = model.generate_content(context + prompt)
  archivo = response.text
  with open("archivo.txt", "w") as f:
    f.write(archivo)

  return archivo

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

################################################################################################
# Título de la aplicación
st.title("CosMOD - Vanguardia de MODA Y COSTURA para toda MODISTA")

# Texto de introducción
st.write("Bienvenido a CosMOD!!, la app que trae lo último en moda y costura a nivel mundial para toda modista, aqui encontraras toda la info que debes saber para estar a la vanguardia a la hora de confeccionar una prenda!")

# Entrada del prompt del usuario
prompt = st.text_area("De forma clara y concisa, escribí aquí, tu consulta sobre la prenda que quieras confeccionar o una determinada moda que quieras conocer: ")

context= "Eres un especialista sobre moda y costura. Analizaras la consulta sobre la prenda a confeccionar, o la consulta sobre la moda en cualquier parte del mundo. Generaras la respuesta mas completa. La prenda o moda que deberas investigar sera la siguiente: "

# Botón para mostrar el nombre
if st.button("Consulta"):
    if prompt:
        # Llamar a la API y obtener la respuesta
        response = consulta(context, prompt),
        
        # Visualizar la respuesta
        st.write(response)
       
    else:
        st.write("No has escrito nada, por favor, escribe tu consulta!!")