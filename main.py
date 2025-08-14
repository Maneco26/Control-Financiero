import streamlit as st
from db.connection import init_db
from modules.tarjetas import ui_tarjetas

init_db()

st.sidebar.title("📂 Módulos")
modulo = st.sidebar.radio("Selecciona un módulo", ["Tarjetas"])

if modulo == "Tarjetas":
    ui_tarjetas()
from modules.servicios import ui_servicios

modulo = st.sidebar.radio("Selecciona un módulo", ["Tarjetas", "Servicios"])

if modulo == "Tarjetas":
    ui_tarjetas()
elif modulo == "Servicios":
    ui_servicios()

from modules.pagos import ui_pagos

modulo = st.sidebar.radio("Selecciona un módulo", ["Tarjetas", "Servicios", "Pagos"])

if modulo == "Tarjetas":
    ui_tarjetas()
elif modulo == "Servicios":
    ui_servicios()
elif modulo == "Pagos":
    ui_pagos()
