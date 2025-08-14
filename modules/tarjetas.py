import streamlit as st
import sqlite3
from db.connection import get_connection

def crear_tarjeta(data):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tarjetas (nombre, emisor, tipo, limite, saldo_actual, fecha_corte, fecha_pago, notas)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, data)
    conn.commit()
    conn.close()

def obtener_tarjetas():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tarjetas")
    tarjetas = cursor.fetchall()
    conn.close()
    return tarjetas

def eliminar_tarjeta(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tarjetas WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def actualizar_tarjeta(id, data):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE tarjetas SET nombre=?, emisor=?, tipo=?, limite=?, saldo_actual=?, fecha_corte=?, fecha_pago=?, notas=?
        WHERE id=?
    """, (*data, id))
    conn.commit()
    conn.close()

def ui_tarjetas():
    st.header("💳 Gestión de Tarjetas")

    with st.form("Nueva tarjeta"):
        nombre = st.text_input("Nombre")
        emisor = st.text_input("Emisor")
        tipo = st.selectbox("Tipo", ["Crédito", "Débito"])
        limite = st.number_input("Límite", min_value=0.0)
        saldo = st.number_input("Saldo actual", min_value=0.0)
        fecha_corte = st.date_input("Fecha de corte")
        fecha_pago = st.date_input("Fecha de pago límite")
        notas = st.text_area("Notas")
        submitted = st.form_submit_button("Agregar")

        if submitted:
            crear_tarjeta((nombre, emisor, tipo, limite, saldo, str(fecha_corte), str(fecha_pago), notas))
            st.success("Tarjeta agregada correctamente")

    st.subheader("📋 Tarjetas registradas")
    tarjetas = obtener_tarjetas()
    for t in tarjetas:
        st.write(f"**{t[1]}** ({t[2]}) - {t[3]} | Límite: {t[4]} | Saldo: {t[5]}")
        col1, col2 = st.columns(2)
        with col1:
            if st.button(f"🗑️ Eliminar {t[0]}", key=f"del_{t[0]}"):
                eliminar_tarjeta(t[0])
                st.experimental_rerun()
        with col2:
            if st.button(f"✏️ Editar {t[0]}", key=f"edit_{t[0]}"):
                st.warning("Función de edición en desarrollo")
