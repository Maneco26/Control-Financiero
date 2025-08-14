def ui_tarjetas():
    st.header("💳 Gestión de Tarjetas")

    # 👉 Formulario para agregar nueva tarjeta
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
            st.experimental_rerun()

    st.subheader("📋 Tarjetas registradas")
    tarjetas = obtener_tarjetas()
    for t in tarjetas:
        with st.expander(f"{t[1]} ({t[2]})"):
            st.write(f"**Límite:** {t[4]} | **Saldo:** {t[5]}")
            st.write(f"**Fecha corte:** {t[6]} | **Fecha pago:** {t[7]}")
            st.write(f"**Notas:** {t[8]}")
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"🗑️ Eliminar", key=f"del_{t[0]}"):
                    eliminar_tarjeta(t[0])
                    st.success("Tarjeta eliminada")
                    st.experimental_rerun()
            with col2:
                if st.button(f"✏️ Editar", key=f"edit_{t[0]}"):
                    with st.form(f"Editar tarjeta {t[0]}"):
                        nombre_e = st.text_input("Nombre", value=t[1])
                        emisor_e = st.text_input("Emisor", value=t[2])
                        tipo_e = st.selectbox("Tipo", ["Crédito", "Débito"], index=0 if t[3] == "Crédito" else 1)
                        limite_e = st.number_input("Límite", value=t[4], min_value=0.0)
                        saldo_e = st.number_input("Saldo actual", value=t[5], min_value=0.0)
                        fecha_corte_e = st.date_input("Fecha de corte", value=t[6])
                        fecha_pago_e = st.date_input("Fecha de pago límite", value=t[7])
                        notas_e = st.text_area("Notas", value=t[8])
                        actualizar = st.form_submit_button("Guardar cambios")

                        if actualizar:
                            actualizar_tarjeta(t[0], (
                                nombre_e, emisor_e, tipo_e, limite_e, saldo_e,
                                str(fecha_corte_e), str(fecha_pago_e), notas_e
                            ))
                            st.success("Tarjeta actualizada")
                            st.experimental_rerun()
