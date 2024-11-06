import streamlit as st

st.title("Demo")

st.sidebar.title("Parametros")


ge = st.number_input("Ingrese el valor de la gravedad especifica", min_value= 0.1, max_value=1.0, value =0.8)

api = (141.5/ge)-131.5

st.write("El valor  del grado api es :", round(api,2))