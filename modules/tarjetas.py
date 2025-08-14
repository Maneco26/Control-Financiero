import streamlit as st
import sqlite3
from datetime import date

DB_PATH = "data/finanzas.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarjetas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            emisor TEXT,
            tipo TEXT CHECK(tipo IN ('Crédito', 'Débito')) NOT NULL,
            limite REAL,
            saldo_actual REAL,
            fecha_corte TEXT,
            fecha_pago_limite TEXT,
            notas TEXT
        )
    """)
    conn.commit()
    conn.close()

def agregar_tarjeta(data):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tarjetas (nombre, emisor, tipo, limite, saldo_actual, fecha_corte, fecha_pago_limite, notas)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, data)
    conn.commit()
    conn.close()

def obtener_tarjetas():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tarjetas")
    tarjetas = cursor.fetchall()
    conn.close()
    return tarjetas

def eliminar_tarjeta(id_tarjeta):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tarjetas WHERE id = ?", (id_tarjeta,))
    conn.commit()
    conn.close()

def ui_tarjetas():
    st.header("💳 Gestión de Tarjetas")
    init_db()

    tabs = st.tabs(["➕ Agregar Tarjeta", "📋 Ver Tarjetas"])

    with tabs[0]:
        with st.form("form_tarjeta"):
            nombre = st.text_input("Nombre de la tarjeta", max_chars=50)
            emisor = st.text_input("Emisor")
            tipo = st.selectbox("Tipo", ["Crédito", "Débito"])
            limite = st.number_input("Límite", min_value=0.0, step=100.0)
            saldo_actual = st.number_input("Saldo actual", min_value=0.0, step=100.0)
            fecha_corte = st.date_input("Fecha de corte", value=date.today())
            fecha_pago_limite = st.date_input("Fecha de pago límite", value=date.today())
            notas = st.text_area("Notas")

            submitted = st.form_submit_button("Guardar")
            if submitted:
                if nombre.strip() == "":
                    st.warning("El nombre es obligatorio.")
                else:
                    agregar_tarjeta((nombre, emisor, tipo, limite, saldo_actual, fecha_corte.isoformat(), fecha_pago_limite.isoformat(), notas))
                    st.success("Tarjeta guardada correctamente.")

    with tabs[1]:
        tarjetas = obtener_tarjetas()
        if tarjetas:
            for t in tarjetas:
                with st.expander(f"{t[1]} ({t[3]})"):
                    st.write(f"**Emisor:** {t[2]}")
                    st.write(f"**Límite:** {t[4]}")
                    st.write(f"**Saldo actual:** {t[5]}")
                    st.write(f"**Fecha de corte:** {t[6]}")
                    st.write(f"**Fecha de pago límite:** {t[7]}")
                    st.write(f"**Notas:** {t[8]}")
                    if st.button(f"🗑️ Eliminar tarjeta {t[0]}", key=f"del_{t[0]}"):
                        eliminar_tarjeta(t[0])
                        st.success("Tarjeta eliminada.")
                        st.experimental_rerun()
        else:
            st.info("No hay tarjetas registradas.")
