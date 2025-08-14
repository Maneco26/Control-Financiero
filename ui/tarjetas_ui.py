import streamlit as st
from services.tarjetas_service import crear_tarjeta, obtener_tarjetas

def mostrar_tarjetas():
    st.header("Registro de Tarjetas")

    with st.form("form_tarjeta"):
        nombre = st.text_input("Nombre")
        emisor = st.text_input("Emisor")
        tipo = st.selectbox("Tipo", ["Crédito", "Débito"])
        limite = st.number_input("Límite", min_value=0.0)
        saldo_actual = st.number_input("Saldo actual", min_value=0.0)
        fecha_corte = st.date_input("Fecha de corte")
        fecha_pago = st.date_input("Fecha de pago")
        notas = st.text_area("Notas")
        divisa = st.selectbox("Divisa", ["Córdobas", "Dólares"])

        submitted = st.form_submit_button("Guardar")
        if submitted:
            crear_tarjeta({
                "nombre": nombre,
                "emisor": emisor,
                "tipo": tipo,
                "limite": limite,
                "saldo_actual": saldo_actual,
                "fecha_corte": fecha_corte,
                "fecha_pago": fecha_pago,
                "notas": notas,
                "divisa": divisa
            })
            st.success("Tarjeta guardada correctamente")

    st.subheader("Tarjetas registradas")
    tarjetas = obtener_tarjetas()
    for t in tarjetas:
        st.write(f"💳 {t.nombre} ({t.tipo}) - Saldo: {t.saldo_actual} {t.divisa}")
