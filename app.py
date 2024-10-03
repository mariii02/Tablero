import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.title ("¡Dibuja lo que quieras!")
st.subheader("Utiliza el trablero de dibujo para hacer arte")


# Add canvas component
# Specify canvas parameters in application

bg_color = '#000000'

with st.sidebar:
    drawing_mode = st.selectbox(
    "Selecciona el tipo de trazo",
    ("freedraw", "line", "rect"),
    )
    stroke_width = st.slider('Selecciona el ancho de línea', 1, 30, 15)
    stroke_color = st.color_picker("Pick A Color", "#00f900")
    st.write("Estás usando el color:",  stroke_color)

# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=400,
    width=400,
    key="canvas",
)
