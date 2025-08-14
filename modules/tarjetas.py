import streamlit as st

def ui_tarjetas():
    st.header("💳 Gestión de Tarjetas")

    with st.form("form_tarjeta"):
        nombre = st.text_input("Nombre de la tarjeta")
        emisor = st.text_input("Emisor")
        tipo = st.selectbox("Tipo", ["Crédito", "Débito"])
        limite = st.number_input("Límite", min_value=0.0)
        saldo = st.number_input("Saldo actual", min_value=0.0)
        fecha_corte = st.date_input("Fecha de corte")
        fecha_pago = st.date_input("Fecha límite de pago")
        notas = st.text_area("Notas")

        submitted = st.form_submit_button("Guardar")
        if submitted:
            st.success("Tarjeta registrada correctamente.")
