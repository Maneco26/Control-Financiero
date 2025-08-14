import streamlit as st
from datetime import date
from database import session
from models.pagos_model import Pago
from models.tarjetas_model import Tarjeta
from models.servicios_model import Servicio

def crear_pago():
    st.subheader("Registrar nuevo pago")

    fecha = st.date_input("Fecha del pago", value=date.today())
    tipo_pago = st.selectbox("Tipo de pago", ["Servicio recurrente", "Tarjeta de crédito", "Otro"])

    tarjeta_id = None
    servicio_id = None
    monto = None
    modo_pago = None

    if tipo_pago == "Servicio recurrente":
        servicios = session.query(Servicio).filter_by(estado="activo").all()
        servicio_opciones = {f"{s.nombre} ({s.proveedor})": s.id for s in servicios}
        servicio_nombre = st.selectbox("Servicio", list(servicio_opciones.keys()))
        servicio_id = servicio_opciones[servicio_nombre]
        servicio = session.get(Servicio, servicio_id)
        monto = st.number_input("Monto", value=servicio.monto_defecto, min_value=0.0)
    
    elif tipo_pago == "Tarjeta de crédito":
        tarjetas = session.query(Tarjeta).all()
        tarjeta_opciones = {f"{t.nombre} ({t.emisor})": t.id for t in tarjetas}
        tarjeta_nombre = st.selectbox("Tarjeta", list(tarjeta_opciones.keys()))
        tarjeta_id = tarjeta_opciones[tarjeta_nombre]
        tarjeta = session.get(Tarjeta, tarjeta_id)

        modo_pago = st.radio("Modo de pago", ["Completo", "Parcial"])
        if modo_pago == "Completo":
            monto = tarjeta.saldo_actual
        else:
            monto = st.number_input("Monto parcial", min_value=0.0)

    else:
        monto = st.number_input("Monto", min_value=0.0)

    referencia = st.text_input("Referencia o nota")

    if st.button("Guardar pago"):
        nuevo_pago = Pago(
            fecha=fecha,
            tipo_pago=tipo_pago,
            tarjeta_id=tarjeta_id,
            servicio_id=servicio_id,
            modo_pago=modo_pago,
            monto=monto,
            referencia=referencia
        )
        session.add(nuevo_pago)
        session.commit()
        st.success("Pago registrado exitosamente.")
