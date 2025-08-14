import streamlit as st
from modules.tarjetas import ui_tarjetas
# Aquí luego importarás otros módulos como:
# from modules.servicios import ui_servicios
# from modules.pagos import ui_pagos
# etc.

# Configuración básica
st.set_page_config(page_title="App Financiera", layout="wide")

# Navegación por pestañas horizontales
tabs = st.tabs(["🏠 Inicio", "💳 Tarjetas", "🧾 Servicios", "💸 Pagos", "📈 Dashboard"])

# 🏠 Inicio
with tabs[0]:
    st.title("📊 Bienvenido a tu App Financiera")
    st.markdown("""
    Esta herramienta está diseñada para darte control total sobre tus finanzas personales.
    
    Usa las pestañas superiores para navegar entre módulos como Tarjetas, Servicios, Pagos y más.
    """)

# 💳 Tarjetas
with tabs[1]:
    ui_tarjetas()

# 🧾 Servicios
with tabs[2]:
    st.info("Módulo de Servicios aún no implementado.")

# 💸 Pagos
with tabs[3]:
    st.info("Módulo de Pagos aún no implementado.")

# 📈 Dashboard
with tabs[4]:
    st.info("Dashboard en construcción.")
