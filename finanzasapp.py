import streamlit as st
import pandas as pd
import datetime as dt


# Título de la app
st.title("App de Finanzas")

# Autor de la app
st.write("Esta app fue elaborada por “Simón Cardona Yepes.")

# Inicialización de datos
if "data" not in st.session_state:
    st.session_state.data = {
        "fecha": [],
        "tipo": [],
        "categoría": [],
        "monto": [],
        "presupuestado": []
    }

# Función para agregar una transacción
def agregar_transaccion(fecha, tipo, categoría, monto, presupuestado):
    st.session_state.data["fecha"].append(fecha)
    st.session_state.data["tipo"].append(tipo)
    st.session_state.data["categoría"].append(categoría)
    st.session_state.data["monto"].append(monto)
    st.session_state.data["presupuestado"].append(presupuestado)

# Función para generar reportes
def generar_reporte(periodo):
    df = pd.DataFrame(st.session_state.data)
    if df.empty:
        return "No hay datos disponibles para generar reportes."
    
    # Filtrar datos por periodo
    fecha_actual = dt.date.today()
    if periodo == "Semanal":
        fecha_inicio = fecha_actual - dt.timedelta(days=7)
    elif periodo == "Mensual":
        fecha_inicio = fecha_actual - dt.timedelta(days=30)

    df["fecha"] = pd.to_datetime(df["fecha"])
    df_periodo = df[df["fecha"] >= fecha_inicio]
    
    # Calcular diferencias entre presupuestado y real
    reporte = df_periodo.groupby(["categoría", "tipo"]).agg(
        Total_Real=("monto", "sum"),
        Total_Presupuestado=("presupuestado", "sum")
    )
    reporte["Diferencia"] = reporte["Total_Real"] - reporte["Total_Presupuestado"]
    return reporte

# Título de la aplicación
st.title("App de Finanzas Personales")

# Sección: Registro de transacciones
st.header("Registro de Transacciones")
fecha = st.date_input("Fecha:", dt.date.today())
tipo = st.selectbox("Tipo:", ["Ingreso", "Gasto"])
categoría = st.selectbox(
    "Categoría:", ["Alimentación", "Transporte", "Vivienda", "Ocio", "Salud", "Educación", "Otros"]
)
monto = st.number_input("Monto:", min_value=0.0, step=0.01)
presupuestado = st.number_input("Monto Presupuestado:", min_value=0.0, step=0.01)

if st.button("Agregar Transacción"):
    agregar_transaccion(fecha, tipo, categoría, monto, presupuestado)
    st.success("Transacción agregada correctamente.")

# Mostrar tabla de transacciones
st.subheader("Historial de Transacciones")
df = pd.DataFrame(st.session_state.data)
if not df.empty:
    st.dataframe(df)
else:
    st.write("No hay transacciones registradas.")

# Sección: Reportes
st.header("Reportes de Finanzas")
periodo = st.selectbox("Selecciona el período para el reporte:", ["Semanal", "Mensual"])
if st.button("Generar Reporte"):
    reporte = generar_reporte(periodo)
    if isinstance(reporte, str):
        st.write(reporte)
    else:
        st.write(f"Reporte {periodo}:")
        st.dataframe(reporte)
