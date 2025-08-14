import streamlit as st
import sqlite3

DB_PATH = "data/finanzas.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS servicios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            monto_defecto REAL,
            periodicidad TEXT,
            proveedor TEXT,
            categoria TEXT,
            estado TEXT CHECK(estado IN ('Activo', 'Inactivo')) NOT NULL,
            notas TEXT
        )
    """)
    conn.commit()
    conn.close()

def agregar_servicio(data):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO servicios (nombre, monto_defecto, periodicidad, proveedor, categoria, estado, notas)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, data)
    conn.commit()
    conn.close()

def obtener_servicios():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM servicios")
    servicios = cursor.fetchall()
    conn.close()
    return servicios

def eliminar_servicio(id_servicio):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM servicios WHERE id = ?", (id_servicio,))
    conn.commit()
    conn.close()

def ui_servicios():
    st.header("🔁 Servicios Recurrentes")
    init_db()

    tabs = st.tabs(["➕ Agregar Servicio", "📋 Ver Servicios"])

    with tabs[0]:
        with st.form("form_servicio"):
            nombre = st.text_input("Nombre del servicio", max_chars=50)
            monto_defecto = st.number_input("Monto por defecto", min_value=0.0, step=10.0)
            periodicidad = st.selectbox("Periodicidad", ["Mensual", "Semanal", "Anual", "Otro"])
            proveedor = st.text_input("Proveedor")
            categoria = st.text_input("Categoría")
            estado = st.selectbox("Estado", ["Activo", "Inactivo"])
            notas = st.text_area("Notas")

            submitted = st.form_submit_button("Guardar")
            if submitted:
                if nombre.strip() == "":
                    st.warning("El nombre es obligatorio.")
                else:
                    agregar_servicio((nombre, monto_defecto, periodicidad, proveedor, categoria, estado, notas))
                    st.success("Servicio guardado correctamente.")

    with tabs[1]:
        servicios = obtener_servicios()
        if servicios:
            for s in servicios:
                with st.expander(f"{s[1]} ({s[5]})"):
                    st.write(f"**Monto por defecto:** {s[2]}")
                    st.write(f"**Periodicidad:** {s[3]}")
                    st.write(f"**Proveedor:** {s[4]}")
                    st.write(f"**Estado:** {s[6]}")
                    st.write(f"**Notas:** {s[7]}")
                    if st.button(f"🗑️ Eliminar servicio {s[0]}", key=f"del_serv_{s[0]}"):
                        eliminar_servicio(s[0])
                        st.success("Servicio eliminado.")
                        st.experimental_rerun()
        else:
            st.info("No hay servicios registrados.")
