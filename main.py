import streamlit as st
from modules.tarjetas import ui_tarjetas
from modules.servicios import ui_servicios
from modules.pagos import ui_pagos

st.set_page_config(page_title="Control Financiero", layout="wide")

st.sidebar.title("📂 Módulos")
modulo = st.sidebar.radio("Selecciona un módulo", ["Tarjetas", "Servicios", "Pagos"])

if modulo == "Tarjetas":
    ui_tarjetas()
elif modulo == "Servicios":
    ui_servicios()
elif modulo == "Pagos":
    ui_pagos()
