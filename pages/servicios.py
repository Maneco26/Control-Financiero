import streamlit as st
from database import get_db
from crud.crud_servicios import crear_servicio, obtener_servicios, actualizar_servicio, eliminar_servicio

st.title("🛠️ Gestión de Servicios Recurrentes")
db = get_db()

# 📋 Mostrar servicios existentes
st.subheader("Servicios registrados")
servicios = obtener_servicios(db, solo_activos=False)
for s in servicios:
    with st.expander(f"{s.nombre} ({s.categoria})"):
        st.write(f"💰 Monto por defecto: {s.monto_defecto}")
        st.write(f"📆 Periodicidad: {s.periodicidad}")
        st.write(f"🏢 Proveedor: {s.proveedor}")
        st.write(f"📝 Notas: {s.notas}")
        estado = "Activo" if s.estado else "Inactivo"
        st.write(f"🔄 Estado: {estado}")

        if st.button(f"🗑️ Eliminar {s.nombre}", key=f"del_{s.id}"):
            eliminar_servicio(db, s.id)
            st.success("Servicio eliminado.")
            st.experimental_rerun()

# ➕ Crear nuevo servicio
st.subheader("Agregar nuevo servicio")
with st.form("nuevo_servicio"):
    nombre = st.text_input("Nombre")
    monto = st.number_input("Monto por defecto", min_value=0.0)
    periodicidad = st.selectbox("Periodicidad", ["Mensual", "Semanal", "Anual"])
    proveedor = st.text_input("Proveedor")
    categoria = st.text_input("Categoría")
    estado = st.checkbox("Activo", value=True)
    notas = st.text_area("Notas")

    submitted = st.form_submit_button("Guardar")
    if submitted:
        servicio_data = {
            "nombre": nombre,
            "monto_defecto": monto,
            "periodicidad": periodicidad,
            "proveedor": proveedor,
            "categoria": categoria,
            "estado": estado,
            "notas": notas
        }
        crear_servicio(db, servicio_data)
        st.success("Servicio creado exitosamente.")
        st.experimental_rerun()
