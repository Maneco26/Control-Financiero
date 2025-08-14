for s in servicios:
    with st.expander(f"{s.nombre} ({s.categoria})"):
        modo_edicion = st.checkbox(f"✏️ Editar {s.nombre}", key=f"edit_{s.id}")

        if modo_edicion:
            with st.form(f"form_edit_{s.id}"):
                nuevo_nombre = st.text_input("Nombre", value=s.nombre)
                nuevo_monto = st.number_input("Monto por defecto", min_value=0.0, value=s.monto_defecto)
                nueva_periodicidad = st.selectbox("Periodicidad", ["Mensual", "Semanal", "Anual"], index=["Mensual", "Semanal", "Anual"].index(s.periodicidad))
                nuevo_proveedor = st.text_input("Proveedor", value=s.proveedor)
                nueva_categoria = st.text_input("Categoría", value=s.categoria)
                nuevo_estado = st.checkbox("Activo", value=s.estado)
                nuevas_notas = st.text_area("Notas", value=s.notas)

                guardar = st.form_submit_button("💾 Guardar cambios")
                if guardar:
                    nuevos_datos = {
                        "nombre": nuevo_nombre,
                        "monto_defecto": nuevo_monto,
                        "periodicidad": nueva_periodicidad,
                        "proveedor": nuevo_proveedor,
                        "categoria": nueva_categoria,
                        "estado": nuevo_estado,
                        "notas": nuevas_notas
                    }
                    actualizar_servicio(db, s.id, nuevos_datos)
                    st.success("Servicio actualizado.")
                    st.experimental_rerun()
        else:
            st.write(f"💰 Monto por defecto: {s.monto_defecto}")
            st.write(f"📆 Periodicidad: {s.periodicidad}")
            st.write(f"🏢 Proveedor: {s.proveedor}")
            st.write(f"📝 Notas: {s.notas}")
            estado = "Activo" if s.estado else "Inactivo"
            st.write(f"🔄 Estado: {estado}")

        if st.button(f"🗑️ Eliminar {s.nombre
