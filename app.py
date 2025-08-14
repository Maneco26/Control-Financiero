import streamlit as st
from ui.tarjetas_ui import mostrar_tarjetas
from ui.pagos_ui import mostrar_pagos

st.set_page_config(page_title="Control Financiero", layout="wide")
st.title("📊 Control Financiero")

tabs = st.tabs(["Tarjetas", "Pagos"])

with tabs[0]:
    mostrar_tarjetas()

with tabs[1]:
    mostrar_pagos()
