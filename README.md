# 🚗 Análisis de Vehículos en Estados Unidos
### Sprint 07 — Desarrollo de Aplicaciones Web | TripleTen Data Science
---

## 📋 Descripción

Aplicación web interactiva desarrollada con **Streamlit** para explorar y visualizar el dataset de vehículos usados en Estados Unidos. Permite al usuario generar visualizaciones dinámicas mediante botones interactivos, con una interfaz de estilo **Blueprint** que combina funcionalidad técnica con una experiencia visual distintiva.

El proyecto forma parte del Sprint 07 del programa de Data Science de TripleTen, enfocado en el desarrollo y despliegue de aplicaciones web de análisis de datos.

---

## 🎯 Funcionalidades

- **Histograma de Años de Fabricación** — distribución de vehículos por año de modelo
- **Histograma por Modelo** — frecuencia de los 20 modelos más populares (sub-vista)
- **Gráfico de Dispersión: Precio vs. Odómetro** — relación entre precio y kilometraje
- **Limpieza de pantalla** — control de estado para reiniciar la visualización
- **Interfaz Blueprint** — diseño con cuadrícula técnica, paleta azul navy y tipografía monospace

---

## 🗂️ Estructura del Proyecto

```
sprint_07_Proyecto/
├── notebooks/
│   └── EDA.ipynb               # Análisis exploratorio de datos
├── app.py                      # Aplicación principal Streamlit
├── vehicles_us.csv             # Dataset de vehículos usados EE.UU.
├── requirements.txt            # Dependencias del proyecto
├── .gitignore
└── README.md
```

---

## 📊 Dataset

El dataset `vehicles_us.csv` contiene anuncios de venta de vehículos usados en Estados Unidos con las siguientes variables principales:

| Variable | Descripción |
|---|---|
| `price` | Precio de venta (USD) |
| `model_year` | Año de fabricación del vehículo |
| `model` | Modelo del vehículo |
| `condition` | Condición general (excellent, good, fair, etc.) |
| `cylinders` | Número de cilindros |
| `fuel` | Tipo de combustible |
| `odometer` | Lectura del odómetro (millas) |
| `transmission` | Tipo de transmisión |
| `type` | Tipo de vehículo (SUV, sedan, truck, etc.) |
| `days_listed` | Días activo en el mercado |

---

## ⚙️ Instalación y Uso Local

### Prerrequisitos

- Python 3.11+
- Conda o virtualenv (recomendado)

### Pasos

```bash
# 1. Clonar el repositorio
git clone https://github.com/iqmancilla-ARI/sprint_07_Proyecto.git
cd sprint_07_Proyecto

# 2. Crear y activar entorno virtual
conda create --name entorno_sprint_07 python=3.11 -y
conda activate entorno_sprint_07

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar la aplicación
streamlit run app.py
```

La aplicación se abrirá automáticamente en `http://localhost:8501`

---

## 📦 Dependencias

```
streamlit
pandas
plotly
```

---

## 🚀 Deployment

La aplicación está configurada para desplegarse en **Render**. El archivo `requirements.txt` es leído automáticamente por Render para construir el entorno de producción.

> **Configuración en Render:**
> - Build Command: `pip install -r requirements.txt`
> - Start Command: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`

---

## 📈 Análisis Exploratorio

El notebook `EDA.ipynb` dentro de la carpeta `notebooks/` contiene el análisis exploratorio completo del dataset, incluyendo:

- Inspección y limpieza de datos
- Análisis de valores nulos y outliers
- Distribuciones univariadas y bivariadas
- Estadísticas descriptivas por categoría

---

## 👤 Autor

**J. Daniel Mancilla Malvaez**
Ingeniero Químico | Data Science & Analytics

[![LinkedIn](https://img.shields.io/badge/LinkedIn-pmomancilla-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pmomancilla)
[![GitHub](https://img.shields.io/badge/GitHub-iqmancilla--ARI-181717?style=flat&logo=github&logoColor=white)](https://github.com/iqmancilla-ARI)

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
