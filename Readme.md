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
│   ├── raw/                     # Dataset original sin modificar
│   └── processed/               # Datos tras limpieza y transformación
│
├── notebooks/
│   └── F2_Definicion.ipynb      # Notebook principal Fase 2
│
├── src/
│   ├── data_loading.py          # Función para carga del dataset
│   ├── evaluation.py            # Funciones para evaluación de resultados
│   ├── features.py              # Funciones para creación o transformación de variables
│   ├── modeling.py              # Funciones para modelado
│   └── preprocessing.py         # Funciones para limpieza y preparación de datos
│
├── docs/                        # Documentación y referencias técnicas
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

Abrir el notebook correspondiente a la fase activa:

- **Fase 2:** `notebooks/F2_Definicion.ipynb`

Ejecutar todas las celdas mediante la opción **Kernel → Restart & Run All** para verificar la correcta configuración del entorno y la reproducibilidad del proyecto.

---

## Fase 2 — Pipeline de preprocesamiento

En la Fase 2 se construyó un pipeline completo de procesamiento de datos que incluye:

1. **Carga y exploración inicial** — diagnóstico del dataset (dimensiones, tipos, nulos, duplicados).
2. **Limpieza de datos** — eliminación de duplicados e imputación de valores faltantes.
3. **Transformación y encoding** — encoding ordinal para `Education_Level` y `Risk_Category`; One-Hot Encoding para `Job_Title`.
4. **Feature engineering** — creación de `Skill_Index` (promedio de habilidades) y `High_Risk` (variable objetivo binaria).
5. **Normalización** — escalamiento al rango [0, 1] con `MinMaxScaler` para variables de escala amplia.
6. **Validación** — verificación de rangos, tipos y ausencia de nulos/duplicados.
7. **Exportación** — dataset limpio exportado a `data/processed/AI_Impact_on_Jobs_2030_clean.csv`.

Las funciones del pipeline están implementadas en `src/preprocessing.py` y son invocadas desde el notebook `notebooks/F2_Definicion.ipynb`.

---

## Commits informativos

docs: actualiza README con nueva estructura del repositorio, Nicolás Soletic
merge main into docs/readme-sebastian, Sebastian Navarrete
docs: actualiza README con información del proyecto, Sebastian Navarrete
Se completa el archivo .gitignore,  artu-knopke
Se completa archivo requirements.txt,  artu-knopke
Creación notebook, robertomoncada-blip
Primera subida repositorio estructura base,  robertomoncada-blip



---

## Integrantes

- Arturo Knope Vera  
- Nicolás Soletic Cobos  
- Roberto Moncada González
- Sebastián Navarrete Soto  

**Docente:** Omar Salinas Silva  
**Curso:** MCDI500 — Herramientas de Software Científico  
**Universidad Andrés Bello — Magíster en Ciencia de Datos e Inteligencia Artificial**


