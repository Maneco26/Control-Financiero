import streamlit as st
import pandas as pd

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

st.title("💳 Gestión de Tarjetas")

# Formulario
with st.form("form_tarjeta"):
    nombre = st.text_input("Nombre de la tarjeta")
    emisor = st.text_input("Emisor")
    tipo = st.selectbox("Tipo", ["Crédito", "Débito"])
    limite = st.number_input("Límite", min_value=0.0, step=100.0)
    saldo = st.number_input("Saldo actual", min_value=0.0, step=100.0)
    divisa = st.selectbox("Divisa", ["Córdobas", "Dólares"])
    fecha_corte = st.date_input("Fecha de corte")
    fecha_pago = st.date_input("Fecha de pago límite")
    notas = st.text_area("Notas")

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

        # Limpieza de campos
        st.experimental_rerun()

# Mostrar tarjetas
st.subheader("📋 Tarjetas registradas")
if not st.session_state.tarjetas_db.empty:
    st.dataframe(st.session_state.tarjetas_db.drop(columns=["ID"]), use_container_width=True)

    # Selección para editar o eliminar
    selected = st.selectbox("Selecciona una tarjeta para editar o eliminar", st.session_state.tarjetas_db["ID"])

    col1, col2 = st.columns(2)
    if col1.button("✏️ Editar"):
        st.session_state.edit_index = st.session_state.tarjetas_db[st.session_state.tarjetas_db["ID"] == selected].index[0]
        tarjeta = st.session_state.tarjetas_db.iloc[st.session_state.edit_index]
        st.experimental_rerun()

    if col2.button("🗑️ Eliminar"):
        st.session_state.tarjetas_db = st.session_state.tarjetas_db[st.session_state.tarjetas_db["ID"] != selected].reset_index(drop=True)
        st.success("Tarjeta eliminada.")
        st.experimental_rerun()
else:
    st.info("No hay tarjetas registradas aún.")
