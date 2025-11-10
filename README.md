# ✈️ SimuTravel - Frontend y Backend con Streamlit

Este proyecto muestra los paneles **Viajero** y **Admin** dentro de aplicaciones Streamlit, sin modificar los archivos HTML, CSS ni JS originales.

## 📁 Estructura

```
simutravel-streamlit/
├─ frontend/   # contiene viajero.html, .css, .js
├─ backend/    # contiene admin.html, .css, .js
├─ data/       # contiene data.json
├─ viajero_app.py
├─ admin_app.py
└─ requirements.txt
```

## 🚀 Cómo ejecutarlo

1. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```

2. Abre dos terminales:

   **Terminal 1 (Viajero):**
   ```bash
   streamlit run viajero_app.py
   ```

   **Terminal 2 (Admin):**
   ```bash
   streamlit run admin_app.py
   ```

3. Abre los enlaces que aparecen en tu navegador (por defecto http://localhost:8501 y :8502).

## ☁️ Despliegue

Sube este repositorio a **GitHub** y publícalo en **Streamlit Cloud**:
- Crea una app para `viajero_app.py`
- Otra para `admin_app.py`
