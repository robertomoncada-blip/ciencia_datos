# Impacto de la IA en el empleo - 2030

## Descripción del proyecto

Este proyecto forma parte de la asignatura **MCDI500 – Herramientas de Software Científico**
del **Magíster en Ciencia de Datos e Inteligencia Artificial** de la Universidad Andrés Bello.

El proyecto tiene como propósito analizar el posible impacto de la inteligencia artificial
sobre distintas ocupaciones laborales hacia el año 2030, utilizando herramientas de ciencia
de datos aplicadas al conjunto de datos **AI Impact on Jobs 2030**.

Durante esta primera fase se implementó un entorno de trabajo reproducible, una estructura
organizada del repositorio, documentación técnica inicial y mecanismos de control de versiones
que servirán de base para las etapas posteriores del proyecto.

---

## Pregunta orientadora

**¿Cómo podría impactar la adopción de la Inteligencia Artificial en las distintas ocupaciones
laborales hacia el año 2030 de acuerdo con las variables contenidas en el dataset seleccionado?**

---

## Objetivo general

Analizar el impacto potencial de la inteligencia artificial sobre las ocupaciones laborales
hacia el año 2030 mediante la exploración y análisis de las variables contenidas en el dataset
AI Impact on Jobs 2030.

---

## Estructura del repositorio

```text
ciencia_datos/
│
├── data/
│   ├── raw/               # Dataset original sin modificar
│   └── processed/         # Datos tras limpieza y transformación
│
├── notebooks/
│   └── F1_Definicion.ipynb
│
├── src/
│   └── cargar_datos.py           # Funciones reutilizables (carga de datos, etc.)
│
├── docs/                  # Documentación y referencias técnicas
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Dataset

El dataset utilizado es **AI Impact on Jobs 2030**, disponible en Kaggle:  
https://www.kaggle.com/datasets/khushikyad001/ai-impact-on-jobs-2030

El archivo debe almacenarse en: `data/raw/AI_Impact_on_Jobs_2030.csv`

---

## Requisitos

- Python 3.12.10
- Git
- Jupyter Notebook o JupyterLab

---

## Instalación

**1. Clonar el repositorio:**
```bash
git clone <URL_REPOSITORIO>
cd ciencia_datos
```

**2. Crear entorno virtual:**
```bash
python -m venv .venv
```

**3. Activar entorno virtual:**
```bash
# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate
```

**4. Instalar dependencias:**
```bash
pip install -r requirements.txt
```

---

## Ejecución

**Iniciar JupyterLab:**
```bash
jupyter lab
```

**Abrir y ejecutar el notebook:**

Abrir el notebook:

`notebooks/F1_Definicion.ipynb`

Posteriormente, ejecutar todas las celdas mediante la opción **Kernel → Restart & Run All** para verificar la correcta configuración del entorno y la reproducibilidad del proyecto.

---

## Integrantes

- Arturo Knope Vera  
- Nicolás Soletic Cobos  
- Roberto Moncada González
- Sebastián Navarrete Soto  

**Docente:** Omar Salinas Silva  
**Curso:** MCDI500 — Herramientas de Software Científico  
**Universidad Andrés Bello — Magíster en Ciencia de Datos e Inteligencia Artificial**