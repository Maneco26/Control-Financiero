import streamlit as st
import pandas as pd

def ui_tarjetas():
    # Simulación de base de datos en sesión
    if "tarjetas_db" not in st.session_state:
        st.session_state.tarjetas_db = pd.DataFrame(columns=[
            "ID", "Nombre", "Emisor", "Tipo", "Límite", "Saldo", "Divisa", 
            "Saldo_Córdobas", "Fecha Corte", "Fecha Pago", "Notas"
        ])
    if "edit_index" not in st.session_state:
        st.session_state.edit_index = None

    # Tipo de cambio
    TIPO_CAMBIO = 36.62

    st.header("💳 Gestión de Tarjetas")

    # Si se está editando, precargar datos
    if st.session_state.edit_index is not None:
        tarjeta = st.session_state.tarjetas_db.iloc[st.session_state.edit_index]
        nombre_default = tarjeta["Nombre"]
        emisor_default = tarjeta["Emisor"]
        tipo_default = tarjeta["Tipo"]
        limite_default = tarjeta["Límite"]
        saldo_default = tarjeta["Saldo"]
        divisa_default = tarjeta["Divisa"]
        fecha_corte_default = tarjeta["Fecha Corte"]
        fecha_pago_default = tarjeta["Fecha Pago"]
        notas_default = tarjeta["Notas"]
    else:
        nombre_default = ""
        emisor_default = ""
        tipo_default = "Crédito"
        limite_default = 0.0
        saldo_default = 0.0
        divisa_default = "Córdobas"
        fecha_corte_default = pd.to_datetime("today")
        fecha_pago_default = pd.to_datetime("today")
        notas_default = ""

    # Formulario
    with st.form("form_tarjeta"):
        nombre = st.text_input("Nombre de la tarjeta", value=nombre_default)
        emisor = st.text_input("Emisor", value=emisor_default)
        tipo = st.selectbox("Tipo", ["Crédito", "Débito"], index=["Crédito", "Débito"].index(tipo_default))
        limite = st.number_input("Límite", min_value=0.0, step=100.0, value=limite_default)
        saldo = st.number_input("Saldo actual", min_value=0.0, step=100.0, value=saldo_default)
        divisa = st.selectbox("Divisa", ["Córdobas", "Dólares"], index=["Córdobas", "Dólares"].index(divisa_default))
        fecha_corte = st.date_input("Fecha de corte", value=fecha_corte_default)
        fecha_pago = st.date_input("Fecha de pago límite", value=fecha_pago_default)
        notas = st.text_area("Notas", value=notas_default)

        submitted = st.form_submit_button("Guardar")

        if submitted:
            saldo_cordobas = saldo if divisa == "Córdobas" else round(saldo * TIPO_CAMBIO, 2)

            tarjeta_data = {
                "ID": len(st.session_state.tarjetas_db) + 1 if st.session_state.edit_index is None else st.session_state.edit_index + 1,
                "Nombre": nombre,
                "Emisor": emisor,
                "Tipo": tipo,
                "Límite": limite,
                "Saldo": saldo,
                "Divisa": divisa,
                "Saldo_Córdobas": saldo_cordobas,
                "Fecha Corte": fecha_corte,
                "Fecha Pago": fecha_pago,
                "Notas": notas
            }

            if st.session_state.edit_index is None:
                st.session_state.tarjetas_db = pd.concat([
                    st.session_state.tarjetas_db,
                    pd.DataFrame([tarjeta_data])
                ], ignore_index=True)
                st.success("Tarjeta guardada exitosamente.")
            else:
                st.session_state.tarjetas_db.iloc[st.session_state.edit_index] = tarjeta_data
                st.success("Tarjeta modificada exitosamente.")
                st.session_state.edit_index = None

            st.experimental_rerun()

    # Mostrar tarjetas
    st.subheader("📋 Tarjetas registradas")
    if not st.session_state.tarjetas_db.empty:
        st.dataframe(st.session_state.tarjetas_db.drop(columns=["ID"]), use_container_width=True)

        selected = st.selectbox("Selecciona una tarjeta para editar o eliminar", st.session_state.tarjetas_db["ID"])

        col1, col2 = st.columns(2)
        if col1.button("✏️ Editar"):
            selected_rows = st.session_state.tarjetas_db[st.session_state.tarjetas_db["ID"] == selected]
            if not selected_rows.empty:
                st.session_state.edit_index = selected_rows.index[0]
                st.experimental_rerun()
            else:
                st.warning("La tarjeta seleccionada no existe o fue eliminada.")

        if col2.button("🗑️ Eliminar"):
            st.session_state.tarjetas_db = st.session_state.tarjetas_db[st.session_state.tarjetas_db["ID"] != selected].reset_index(drop=True)
            st.success("Tarjeta eliminada.")
            st.experimental_rerun()
    else:
        st.info("No hay tarjetas registradas aún.")
