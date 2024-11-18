import streamlit as st
import pandas as pd
import requests
import plotly.express as px

# Función para obtener datos de razas de gatos desde The Cat API
def obtener_datos_gatos():
    url = "https://api.thecatapi.com/v1/breeds"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Error al obtener datos de razas. Intenta nuevamente más tarde.")
        return []

# Cargar datos iniciales
st.title("Pronóstico de Salud de Mascotas 🐾")
st.write("Esta app fue elaborada por “Simón Cardona Yepes.")
st.markdown("""
Bienvenido a la app de pronóstico de salud para gatos. Aquí puedes:
- Obtener recomendaciones personalizadas basadas en la edad y raza de tu gato.
- Explorar gráficos sobre la esperanza de vida de diferentes razas.
- Planificar mejores cuidados para tu mascota.
""")

# Obtener datos de razas
razas_data = obtener_datos_gatos()

if razas_data:
    # Crear DataFrame con la información relevante
    df_razas = pd.DataFrame(razas_data)
    df_razas = df_razas[["name", "life_span", "temperament", "weight"]]
    df_razas["vida_min"] = df_razas["life_span"].apply(lambda x: int(x.split(" - ")[0]))
    df_razas["vida_max"] = df_razas["life_span"].apply(lambda x: int(x.split(" - ")[1]))
    df_razas["vida_promedio"] = (df_razas["vida_min"] + df_razas["vida_max"]) / 2

    # Input del usuario
    st.sidebar.header("Datos de tu mascota")
    nombre = st.sidebar.text_input("Nombre de tu gato:")
    raza = st.sidebar.selectbox("Selecciona la raza:", df_razas["name"])
    edad = st.sidebar.number_input("Edad (años):", min_value=0, step=1)
    ejercicio = st.sidebar.slider("Nivel de ejercicio semanal (horas):", 0, 20, 5)
    dieta = st.sidebar.selectbox("Calidad de dieta:", ["Básica", "Equilibrada", "Premium"])
    chequeos = st.sidebar.slider("Chequeos veterinarios al año:", 0, 4, 2)

    # Pronóstico de salud
    st.header(f"Pronóstico de salud para {nombre}")
    raza_seleccionada = df_razas[df_razas["name"] == raza].iloc[0]
    esperanza_vida = raza_seleccionada["vida_promedio"]
    
    if edad > esperanza_vida:
        st.warning(f"{nombre} ya ha superado la esperanza de vida promedio para su raza ({esperanza_vida} años). ¡Cuídalo aún más!")
    else:
        salud = 100 - ((edad / esperanza_vida) * 50) - (10 - ejercicio) - (0 if dieta == "Premium" else (10 if dieta == "Equilibrada" else 20)) - ((2 - chequeos) * 5)
        salud = max(salud, 10)  # La salud no puede bajar de 10
        st.success(f"La salud proyectada de {nombre} es del {salud:.1f}%.")

    # Gráfico de barras: esperanza de vida promedio por raza
    st.subheader("Esperanza de vida promedio por raza")
    fig1 = px.bar(df_razas, x="name", y="vida_promedio", color="vida_promedio",
                  labels={"name": "Raza", "vida_promedio": "Esperanza de vida (años)"},
                  title="Esperanza de vida promedio según la raza")
    st.plotly_chart(fig1)

    # Gráfico de líneas: relación salud vs edad
    st.subheader("Salud proyectada en el tiempo")
    proyeccion_edad = pd.DataFrame({
        "Edad": range(1, int(esperanza_vida) + 1),
        "Salud": [100 - ((i / esperanza_vida) * 50) for i in range(1, int(esperanza_vida) + 1)]
    })
    fig2 = px.line(proyeccion_edad, x="Edad", y="Salud",
                   labels={"Edad": "Edad (años)", "Salud": "Salud (%)"},
                   title="Proyección de salud a lo largo de los años")
    st.plotly_chart(fig2)

    # Recomendaciones
    st.header("Recomendaciones personalizadas")
    st.markdown("""
    Basándonos en la información proporcionada, estas son algunas recomendaciones para mejorar la salud de tu mascota:
    - **Dieta**: Considera una dieta Premium para maximizar la salud.
    - **Ejercicio**: Asegúrate de que tu gato tenga al menos 10 horas de actividad semanal.
    - **Chequeos veterinarios**: Realiza al menos 2 visitas al veterinario al año para prevención.
    """)
else:
    st.error("No se pudieron cargar los datos de razas. Verifica tu conexión o intenta más tarde.")
