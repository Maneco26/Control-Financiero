import streamlit as st

def ui_servicios():
    st.header("🔌 Gestión de Servicios Recurrentes")

    with st.form("form_servicio"):
        nombre = st.text_input("Nombre del servicio")
        monto = st.number_input("Monto por defecto", min_value=0.0)
        periodicidad = st.selectbox("Periodicidad", ["Mensual", "Semanal", "Anual"])
        proveedor = st.text_input("Proveedor")
        categoria = st.text_input("Categoría")
        estado = st.selectbox("Estado", ["Activo", "Inactivo"])
        notas = st.text_area("Notas")

        submitted = st.form_submit_button("Guardar")
        if submitted:
            st.success("Servicio registrado correctamente.")
