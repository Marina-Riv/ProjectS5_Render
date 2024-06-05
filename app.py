import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para los modelos disponibles en venta')
    fig = px.histogram(car_data, x="model")
    st.plotly_chart(fig, use_container_width=True)


build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    st.write('Construir un histograma para la columna model')
