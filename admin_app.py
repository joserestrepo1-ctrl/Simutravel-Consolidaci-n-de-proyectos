import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="SimuTravel - Admin", page_icon="🛂", layout="wide")

st.title("🛂 SimuTravel - Panel del Administrador")

html_path = Path("backend/admin.html")
if html_path.exists():
    html_code = html_path.read_text(encoding="utf-8")
    components.html(html_code, height=900, scrolling=True)
else:
    st.error("No se encontró el archivo admin.html en la carpeta /backend")
