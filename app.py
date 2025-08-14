import streamlit as st
from pages.pagos import crear_pago
# Puedes importar otros módulos cuando estén listos:
# from pages.tarjetas import gestionar_tarjetas
# from pages.servicios import gestionar_servicios

st.set_page_config(page_title="App Financiera", layout="wide")

st.title("📊 Creador de App Financiera")

tabs = st.tabs([
    "Pagos",
    "Tarjetas",
    "Servicios",
    "Ingresos",
    "Gastos",
    "Calendario",
    "Dashboard"
])

with tabs[0]:
    crear_pago()

# Puedes ir activando los demás módulos así:
# with tabs[1]:
#     gestionar_tarjetas()

# with tabs[2]:
#     gestionar_servicios()
