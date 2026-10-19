import streamlit as st
import pandas as pd

st.set_page_config(page_title="Control de Pintura RHC", layout="wide")

st.sidebar.title("RHC Estructuras")
menu = st.sidebar.radio("Navegación:", [
    "📊 1. Dashboard (Gerencia)", 
    "🏭 2. Almacén y Stock", 
    "📋 3. Órdenes de Trabajo (OT)"
])

if menu == "📊 1. Dashboard (Gerencia)":
    st.title("Reporte Gerencial de Costos")
    st.write("Aquí consolidaremos los dólares por metro cuadrado por proyecto.")

elif menu == "🏭 2. Almacén y Stock":
    st.title("Control de Inventario")
    st.write("Ingreso de pintura a Almacén Principal, Prometal Roca y CasaVerde.")

elif menu == "📋 3. Órdenes de Trabajo (OT)":
    st.title("Gestión de OTs y Consumo")
    st.write("Registro de sistema de pintura, granallado, capas y mils por proyecto.")