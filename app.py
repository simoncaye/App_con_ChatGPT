import streamlit as st

# Título de la app
st.title("Mi primera app")

# Autor de la app
st.write("Esta app fue elaborada por “Simón Cardona Yepes.")

# Función para conversiones
def realizar_conversion(categoria, tipo_conversion, valor):
    if categoria == "Temperatura":
        if tipo_conversion == "Celsius a Fahrenheit":
            return (valor * 9/5) + 32
        elif tipo_conversion == "Fahrenheit a Celsius":
            return (valor - 32) * 5/9
        elif tipo_conversion == "Celsius a Kelvin":
            return valor + 273.15
        elif tipo_conversion == "Kelvin a Celsius":
            return valor - 273.15

    elif categoria == "Longitud":
        if tipo_conversion == "Pies a Metros":
            return valor * 0.3048
        elif tipo_conversion == "Metros a Pies":
            return valor / 0.3048
        elif tipo_conversion == "Pulgadas a Centímetros":
            return valor * 2.54
        elif tipo_conversion == "Centímetros a Pulgadas":
            return valor / 2.54

    elif categoria == "Peso/Masa":
        if tipo_conversion == "Libras a Kilogramos":
            return valor * 0.453592
        elif tipo_conversion == "Kilogramos a Libras":
            return valor / 0.453592
        elif tipo_conversion == "Onzas a Gramos":
            return valor * 28.3495
        elif tipo_conversion == "Gramos a Onzas":
            return valor / 28.3495

    elif categoria == "Volumen":
        if tipo_conversion == "Galones a Litros":
            return valor * 3.78541
        elif tipo_conversion == "Litros a Galones":
            return valor / 3.78541
        elif tipo_conversion == "Pulgadas cúbicas a Centímetros cúbicos":
            return valor * 16.3871
        elif tipo_conversion == "Centímetros cúbicos a Pulgadas cúbicas":
            return valor / 16.3871

    elif categoria == "Tiempo":
        if tipo_conversion == "Horas a Minutos":
            return valor * 60
        elif tipo_conversion == "Minutos a Segundos":
            return valor * 60
        elif tipo_conversion == "Días a Horas":
            return valor * 24
        elif tipo_conversion == "Semanas a Días":
            return valor * 7

    elif categoria == "Velocidad":
        if tipo_conversion == "Millas por hora a Kilómetros por hora":
            return valor * 1.60934
        elif tipo_conversion == "Kilómetros por hora a Metros por segundo":
            return valor / 3.6
        elif tipo_conversion == "Nudos a Millas por hora":
            return valor * 1.15078
        elif tipo_conversion == "Metros por segundo a Pies por segundo":
            return valor * 3.28084

    elif categoria == "Área":
        if tipo_conversion == "Metros cuadrados a Pies cuadrados":
            return valor * 10.7639
        elif tipo_conversion == "Pies cuadrados a Metros cuadrados":
            return valor / 10.7639
        elif tipo_conversion == "Kilómetros cuadrados a Millas cuadradas":
            return valor * 0.386102
        elif tipo_conversion == "Millas cuadradas a Kilómetros cuadrados":
            return valor / 0.386102

    elif categoria == "Energía":
        if tipo_conversion == "Julios a Calorías":
            return valor / 4.184
        elif tipo_conversion == "Calorías a Kilojulios":
            return valor * 0.004184
        elif tipo_conversion == "Kilovatios-hora a Megajulios":
            return valor * 3.6
        elif tipo_conversion == "Megajulios a Kilovatios-hora":
            return valor / 3.6

    elif categoria == "Presión":
        if tipo_conversion == "Pascales a Atmósferas":
            return valor / 101325
        elif tipo_conversion == "Atmósferas a Pascales":
            return valor * 101325
        elif tipo_conversion == "Barras a Libras por pulgada cuadrada":
            return valor * 14.5038
        elif tipo_conversion == "Libras por pulgada cuadrada a Barras":
            return valor / 14.5038

    elif categoria == "Tamaño de datos":
        if tipo_conversion == "Megabytes a Gigabytes":
            return valor / 1024
        elif tipo_conversion == "Gigabytes a Terabytes":
            return valor / 1024
        elif tipo_conversion == "Kilobytes a Megabytes":
            return valor / 1024
        elif tipo_conversion == "Terabytes a Petabytes":
            return valor / 1024

# Título de la app
st.title("Conversor Universal")

# Selección de la categoría
categoria = st.selectbox(
    "Selecciona una categoría:",
    ["Temperatura", "Longitud", "Peso/Masa", "Volumen", "Tiempo", "Velocidad", "Área", "Energía", "Presión", "Tamaño de datos"]
)

# Opciones de conversión
conversiones = {
    "Temperatura": ["Celsius a Fahrenheit", "Fahrenheit a Celsius", "Celsius a Kelvin", "Kelvin a Celsius"],
    "Longitud": ["Pies a Metros", "Metros a Pies", "Pulgadas a Centímetros", "Centímetros a Pulgadas"],
    "Peso/Masa": ["Libras a Kilogramos", "Kilogramos a Libras", "Onzas a Gramos", "Gramos a Onzas"],
    "Volumen": ["Galones a Litros", "Litros a Galones", "Pulgadas cúbicas a Centímetros cúbicos", "Centímetros cúbicos a Pulgadas cúbicas"],
    "Tiempo": ["Horas a Minutos", "Minutos a Segundos", "Días a Horas", "Semanas a Días"],
    "Velocidad": ["Millas por hora a Kilómetros por hora", "Kilómetros por hora a Metros por segundo", "Nudos a Millas por hora", "Metros por segundo a Pies por segundo"],
    "Área": ["Metros cuadrados a Pies cuadrados", "Pies cuadrados a Metros cuadrados", "Kilómetros cuadrados a Millas cuadradas", "Millas cuadradas a Kilómetros cuadrados"],
    "Energía": ["Julios a Calorías", "Calorías a Kilojulios", "Kilovatios-hora a Megajulios", "Megajulios a Kilovatios-hora"],
    "Presión": ["Pascales a Atmósferas", "Atmósferas a Pascales", "Barras a Libras por pulgada cuadrada", "Libras por pulgada cuadrada a Barras"],
    "Tamaño de datos": ["Megabytes a Gigabytes", "Gigabytes a Terabytes", "Kilobytes a Megabytes", "Terabytes a Petabytes"]
}

tipo_conversion = st.selectbox("Selecciona el tipo de conversión:", conversiones[categoria])

# Entrada de valor
valor = st.number_input("Ingresa el valor a convertir:")

# Realizar conversión
if st.button("Convertir"):
    resultado = realizar_conversion(categoria, tipo_conversion, valor)
    st.write(f"Resultado: {resultado}")
