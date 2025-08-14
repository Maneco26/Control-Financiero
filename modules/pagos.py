import streamlit as st
from db.connection import get_connection

def crear_pago(data):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO pagos (fecha, tipo_pago, servicio_id, tarjeta_id, modo_pago, monto, referencia)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, data)
    conn.commit()
    conn.close()

def obtener_servicios():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, monto_defecto FROM servicios WHERE estado = 'Activo'")
    return cursor.fetchall()

def obtener_tarjetas():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, saldo_actual FROM tarjetas")
    return cursor.fetchall()

def obtener_pagos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pagos ORDER BY fecha DESC")
    return cursor.fetchall()

def ui_pagos():
    st.header("💸 Registro de Pagos")

    servicios = obtener_servicios()
    tarjetas = obtener_tarjetas()

    with st.form("Nuevo pago"):
        fecha = st.date_input("Fecha del pago")
        tipo_pago = st.selectbox("Tipo de pago", ["Servicio", "Tarjeta"])

        servicio_id = None
        tarjeta_id = None
        modo_pago = None
        monto = 0.0

        if tipo_pago == "Servicio":
            servicio = st.selectbox("Servicio", servicios, format_func=lambda x: x[1])
            servicio_id = servicio[0]
            monto = servicio[2]
            st.info(f"Monto sugerido: {monto}")
        elif tipo_pago == "Tarjeta":
            tarjeta = st.selectbox("Tarjeta", tarjetas, format_func=lambda x: x[1])
            tarjeta_id = tarjeta[0]
            modo_pago = st.radio("Modo de pago", ["Completo", "Parcial"])
            if modo_pago == "Completo":
                monto = tarjeta[2]
                st.info(f"Pago completo: {monto}")
            else:
                monto = st.number_input("Monto parcial", min_value=0.0)

        referencia = st.text_input("Referencia / Nota")
        submitted = st.form_submit_button("Registrar pago")

        if submitted:
            crear_pago((
                str(fecha), tipo_pago, servicio_id, tarjeta_id,
                modo_pago, monto, referencia
            ))
            st.success("Pago registrado correctamente")
            st.experimental_rerun()

    st.subheader("📋 Pagos registrados")
    pagos = obtener_pagos()
    for p in pagos:
        st.write(f"{p[1]} | {p[2]} | Monto: {p[6]} | Ref: {p[7]}")
