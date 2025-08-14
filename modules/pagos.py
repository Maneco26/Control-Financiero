import streamlit as st

def ui_pagos():
    st.header("💸 Registro de Pagos")

    with st.form("form_pago"):
        fecha = st.date_input("Fecha del pago")
        tipo_pago = st.selectbox("Tipo de pago", ["Servicio recurrente", "Tarjeta de crédito"])
        tarjeta = st.text_input("Tarjeta asociada (si aplica)")
        modo_pago = st.selectbox("Modo de pago", ["Completo", "Parcial"])
        monto = st.number_input("Monto", min_value=0.0)
        referencia = st.text_area("Referencia / Nota")

        submitted = st.form_submit_button("Guardar")
        if submitted:
            st.success("Pago registrado correctamente.")
