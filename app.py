import streamlit as st
import pandas as pd
import plotly.express as px

# Leer el archivo CSV
file_path = 'C:/Users/MAYRA ROCIO/OneDrive/Escritorio/proyecto vehiculos/vehicles_us/vehicles_us.csv'
df = pd.read_csv(file_path)

# Encabezado
st.header('Histograma de Precios de Vehículos')

# Botón para generar el histograma
if st.button('Generar Histograma'):
    # Crear histograma utilizando Plotly Express
    fig = px.histogram(df, x='price', title='Histograma de Precios')
    # Mostrar el histograma
    st.plotly_chart(fig)


import streamlit as st
import pandas as pd
import plotly.express as px

# Lee el archivo CSV en un DataFrame
file_path = 'C:/Users/MAYRA ROCIO/OneDrive/Escritorio/proyecto vehiculos/vehicles_us/vehicles_us.csv'
df = pd.read_csv(file_path)

# Función para construir el histograma
def histogram():
    st.write("Histograma de...")
    fig = px.histogram(df, x='price')
    st.plotly_chart(fig)

# Función para construir el gráfico de dispersión
def scatter_plot():
    st.write("Gráfico de dispersión de...")
    fig = px.scatter(df, x='price', y='model_year')
    st.plotly_chart(fig)

# Botón para construir el histograma
if st.button("Mostrar Histograma"):
    histogram()

# Botón para construir el gráfico de dispersión
if st.button("Mostrar Gráfico de Dispersión"):
    scatter_plot()

import os

# Ruta del archivo
file_path = 'C:/Users/MAYRA ROCIO/OneDrive/Escritorio/proyecto vehiculos/vehicles_us/vehicles_us.csv'

# Imprimir la ruta del archivo
print("Ruta del archivo:", file_path)

# Verificar si el archivo existe en la ruta especificada
if os.path.exists(file_path):
    print("El archivo existe en la ruta especificada.")
else:
    print("El archivo NO existe en la ruta especificada.")

