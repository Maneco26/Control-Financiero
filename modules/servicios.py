import streamlit as st
from db.connection import get_connection

def crear_servicio(data):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO servicios (nombre, monto_defecto, periodicidad, proveedor, categoria, estado, notas)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, data)
    conn.commit()
    conn.close()

def obtener_servicios():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM servicios")
    servicios = cursor.fetchall()
    conn.close()
    return servicios

def eliminar_servicio(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM servicios WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def actualizar_servicio(id, data):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE servicios SET nombre=?, monto_defecto=?, periodicidad=?, proveedor=?, categoria=?, estado=?, notas=?
        WHERE id=?
    """, (*data, id))
    conn.commit()
    conn.close()

def ui_servicios():
    st.header("🔁 Servicios recurrentes")

    with st.form("Nuevo servicio"):
        nombre = st.text_input("Nombre del servicio")
        monto = st.number_input("Monto por defecto", min_value=0.0)
        periodicidad = st.selectbox("Periodicidad", ["Mensual", "Semanal", "Anual"])
        proveedor = st.text_input("Proveedor")
        categoria = st.text_input("Categoría")
        estado = st.selectbox("Estado", ["Activo", "Inactivo"])
        notas = st.text_area("Notas")
        submitted = st.form_submit_button("Agregar")

        if submitted:
            crear_servicio((nombre, monto, periodicidad, proveedor, categoria, estado, notas))
            st.success("Servicio agregado correctamente")
            st.experimental_rerun()

    st.subheader("📋 Servicios registrados")
    servicios = obtener_servicios()
    for s in servicios:
        with st.expander(f"{s[1]} ({s[2]} - {s[3]})"):
            st.write(f"Proveedor: {s[4]} | Categoría: {s[5]} | Estado: {s[6]}")
            st.write(f"Notas: {s[7]}")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("🗑️ Eliminar", key=f"del_s_{s[0]}"):
                    eliminar_servicio(s[0])
                    st.success("Servicio eliminado")
                    st.experimental_rerun()
            with col2:
                if st.button("✏️ Editar", key=f"edit_s_{s[0]}"):
                    with st.form(f"Editar servicio {s[0]}"):
                        nombre_e = st.text_input("Nombre", value=s[1])
                        monto_e = st.number_input("Monto", value=s[2], min_value=0.0)
                        periodicidad_e = st.selectbox("Periodicidad", ["Mensual", "Semanal", "Anual"], index=["Mensual", "Semanal", "Anual"].index(s[3]))
                        proveedor_e = st.text_input("Proveedor", value=s[4])
                        categoria_e = st.text_input("Categoría", value=s[5])
                        estado_e = st.selectbox("Estado", ["Activo", "Inactivo"], index=0 if s[6] == "Activo" else 1)
                        notas_e = st.text_area("Notas", value=s[7])
                        actualizar = st.form_submit_button("Guardar cambios")

                        if actualizar:
                            actualizar_servicio(s[0], (
                                nombre_e, monto_e, periodicidad_e, proveedor_e,
                                categoria_e, estado_e, notas_e
                            ))
                            st.success("Servicio actualizado")
                            st.experimental_rerun()
