import streamlit as st
from ui.tarjetas_ui import mostrar_tarjetas

st.set_page_config(page_title="Control Financiero", layout="wide")
st.title("📊 Control Financiero")

tabs = st.tabs(["Tarjetas"])  # Agregaremos más módulos luego

with tabs[0]:
    mostrar_tarjetas()
