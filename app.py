import pandas as pd
import plotly.express as px
import streamlit as st

vehicle_data = pd.read_csv('vehicles_us.csv')
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para los modelos disponibles en venta')
    fig = px.histogram(vehicle_data, x="model")
    st.plotly_chart(fig, use_container_width=True)


build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    st.write('Construir un histograma para la condicion de los vehiculos disponibles')
    fig = px.histogram(vehicle_data, x="condition")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir un diagrama de dispersión')

if scatter_button:
    st.write('Construir un diagrama de dispersión de los precios por tipo de vehiculo')
    fig = px.scatter(vehicle_data, x="type", y="price")
    st.plotly_chart(fig, use_container_width=True)
