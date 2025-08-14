import streamlit as st
from services.pagos_service import crear_pago, obtener_pagos
from services.tarjetas_service import obtener_tarjetas
from datetime import date

def mostrar_pagos():
    st.header("Registro de Pagos")

    tarjetas = obtener_tarjetas()
    tarjeta_nombres = [t.nombre for t in tarjetas]

    with st.form("form_pago"):
        fecha = st.date_input("Fecha del pago", value=date.today())
        tipo_pago = st.selectbox("Tipo de pago", ["Servicio", "Tarjeta"])
        servicio = None
        tarjeta_id = None
        modo_pago = None
        monto = 0.0

        if tipo_pago == "Servicio":
            servicio = st.text_input("Nombre del servicio")
            monto = st.number_input("Monto del servicio", min_value=0.0)
        else:
            tarjeta_nombre = st.selectbox("Tarjeta asociada", tarjeta_nombres)
            tarjeta = next((t for t in tarjetas if t.nombre == tarjeta_nombre), None)
            tarjeta_id = tarjeta.id if tarjeta else None
            modo_pago = st.selectbox("Modo de pago", ["Completo", "Parcial"])
            if modo_pago == "Completo":
                monto = tarjeta.saldo_actual
            else:
                monto = st.number_input("Monto parcial", min_value=0.0)

        referencia = st.text_area("Referencia / Nota")

        submitted = st.form_submit_button("Guardar")
        if submitted:
            crear_pago({
                "fecha": fecha,
                "tipo_pago": tipo_pago,
                "servicio": servicio,
                "tarjeta_id": tarjeta_id,
                "modo_pago": modo_pago,
                "monto": monto,
                "referencia": referencia
            })
            st.success("Pago registrado correctamente")

    st.subheader("Pagos registrados")
    pagos = obtener_pagos()
    for p in pagos:
        st.write(f"📅 {p.fecha} | 💰 {p.monto} | Tipo: {p.tipo_pago} | Ref: {p.referencia}")
