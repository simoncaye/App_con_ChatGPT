import streamlit as st
import pandas as pd

# Configuración inicial
st.title("Calculadora de PAPA")

# Autor de la app
st.write("Esta app fue elaborada por “Simón Cardona Yepes.")
st.markdown("""
Esta app te permite calcular tu PAPA global y por tipología de asignatura, teniendo en cuenta las calificaciones numéricas y los créditos cursados.
""")

# Función para calcular el PAPA
def calcular_papa(data, por_tipologia=False):
    # Filtrar materias con calificación numérica
    data = data[pd.to_numeric(data["calificación"], errors="coerce").notnull()]
    
    # Calcular productos: calificación * créditos
    data["producto"] = data["calificación"] * data["créditos"]
    
    # Calcular PAPA global
    if not por_tipologia:
        suma_productos = data["producto"].sum()
        suma_creditos = data["créditos"].sum()
        if suma_creditos > 0:
            return suma_productos / suma_creditos
        return "No es posible calcular el PAPA con los datos proporcionados."
    
    # Calcular PAPA por tipología
    papa_por_tipologia = data.groupby("tipología").apply(
        lambda x: x["producto"].sum() / x["créditos"].sum()
    )
    return papa_por_tipologia

# Input de datos
st.header("Datos de las materias")
st.markdown("""
Por favor, ingresa la información de tus materias vistas:
- **Nombre de la asignatura**: Nombre descriptivo de la asignatura.
- **Créditos**: Número de créditos de la asignatura.
- **Calificación**: Calificación numérica definitiva obtenida (o dejar en blanco si no aplica).
- **Tipología**: Tipo de asignatura (ej: Obligatoria, Electiva, Nivelatoria).
""")

# Crear tabla de entrada de datos
if "data" not in st.session_state:
    st.session_state["data"] = pd.DataFrame(columns=["asignatura", "créditos", "calificación", "tipología"])

# Formulario para añadir datos
with st.form("formulario"):
    asignatura = st.text_input("Nombre de la asignatura:")
    creditos = st.number_input("Créditos:", min_value=1, step=1)
    calificacion = st.number_input("Calificación (deja en blanco si no aplica):", step=0.1, value=0.0)
    tipologia = st.selectbox("Tipología:", ["Obligatoria", "Electiva", "Nivelatoria"])
    submit = st.form_submit_button("Añadir asignatura")

    # Añadir datos a la tabla
    if submit:
        if asignatura:
            nueva_fila = {
                "asignatura": asignatura,
                "créditos": creditos,
                "calificación": calificacion if calificacion > 0 else None,
                "tipología": tipologia,
            }
            st.session_state["data"] = st.session_state["data"].append(nueva_fila, ignore_index=True)
            st.success(f"Asignatura '{asignatura}' añadida correctamente.")
        else:
            st.error("Por favor, ingresa un nombre para la asignatura.")

# Mostrar tabla de materias
st.subheader("Materias ingresadas")
st.dataframe(st.session_state["data"])

# Botones para calcular el PAPA
st.subheader("Cálculo del PAPA")
opcion = st.radio("Selecciona el cálculo que deseas realizar:", ["PAPA Global", "PAPA por Tipología"])

if st.button("Calcular PAPA"):
    data = st.session_state["data"]
    if data.empty:
        st.error("No se han ingresado datos de materias.")
    else:
        if opcion == "PAPA Global":
            resultado = calcular_papa(data)
            st.success(f"Tu PAPA global es: {resultado:.2f}" if isinstance(resultado, float) else resultado)
        elif opcion == "PAPA por Tipología":
            resultado = calcular_papa(data, por_tipologia=True)
            st.write("Tu PAPA por tipología de asignatura es:")
            st.dataframe(resultado)
