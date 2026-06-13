# Impacto de la IA en el empleo - 2030

## Descripción del proyecto

Este proyecto forma parte de la asignatura **MCDI500 – Herramientas de Software Científico**
del **Magíster en Ciencia de Datos e Inteligencia Artificial** de la Universidad Andrés Bello.

El proyecto tiene como propósito analizar el posible impacto de la inteligencia artificial
sobre distintas ocupaciones laborales hacia el año 2030, utilizando herramientas de ciencia
de datos aplicadas al conjunto de datos **AI Impact on Jobs 2030**.

En las primeras fases del proyecto se implementó un entorno de trabajo reproducible, una estructura organizada del repositorio, documentación técnica y un pipeline de preprocesamiento para la limpieza, transformación, validación y exportación del dataset (Fase 2). En la Fase 3 se encapsuló ese pipeline en una clase Python (`Preprocesador`), se implementaron algoritmos estructurados y recursivos (`merge_sort`, búsqueda binaria), y se midió la complejidad temporal y espacial comparando implementaciones alternativas.

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
├── F3/
│   └── README.md                # Manifiesto de la Fase 3: entregables y cómo ejecutar
│
├── data/
│   ├── raw/                     # Dataset original sin modificar
│   └── processed/               # Datos tras limpieza y transformación
│
├── notebooks/
│   ├── F2_Definicion.ipynb      # Notebook Fase 2: pipeline de preprocesamiento
│   └── F3_Definicion.ipynb      # Notebook Fase 3: algoritmos, POO, mediciones de complejidad
│
├── src/
│   ├── transformadores.py       # (F3) Jerarquía POO: Transformador (ABC), subclases, Pipeline
│   ├── algoritmos.py            # (F3) Algoritmos recursivos: merge_sort, busqueda_binaria
│   ├── Preprocesador.py         # (F3) Clase POO con pipeline encapsulado
│   ├── preprocessing.py         # (F2) Funciones de preprocesamiento
│   ├── data_loading.py          # (F2) Función para carga del dataset
│   ├── evaluation.py            # Funciones para evaluación de resultados
│   ├── features.py              # Funciones para creación o transformación de variables
│   └── modeling.py              # Funciones para modelado
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

**Iniciar JupyterLab desde la raíz del repositorio:**
```bash
jupyter lab
```

> **Importante:** JupyterLab debe iniciarse siempre desde la carpeta raíz `ciencia_datos/`. Las rutas relativas del notebook (`../src`, `../F3/src`, `../data/`) dependen de que el kernel se ejecute desde `notebooks/`.

**Abrir y ejecutar el notebook de Fase 3:**

1. Abrir `notebooks/F3_Definicion.ipynb` desde el explorador de JupyterLab.
2. Ejecutar todas las celdas con **Kernel → Restart & Run All**.
3. El notebook carga automáticamente los módulos desde `src/` (Fase 2) y `F3/src/` (Fase 3).

**Notebooks disponibles:**

| Notebook | Fase | Contenido |
|---|---|---|
| `notebooks/F2_Definicion.ipynb` | Fase 2 | Pipeline de preprocesamiento con funciones |
| `notebooks/F3_Definicion.ipynb` | Fase 3 | Algoritmos, POO (herencia, polimorfismo), mediciones de complejidad |

---

## Solución de problemas

| Problema | Causa probable | Solución |
|---|---|---|
| `ModuleNotFoundError: No module named 'Preprocesador'` | El path a `src/` no se agregó al entorno | Ejecutar las celdas desde el inicio; la primera celda de configuración añade `../src` al `sys.path`. |
| `FileNotFoundError: ../data/raw/AI_Impact_on_Jobs_2030.csv` | El notebook se ejecuta desde un directorio distinto a `notebooks/` | Iniciar JupyterLab desde la raíz del repositorio y abrir el notebook desde `notebooks/`. Las rutas son relativas a esa carpeta. |
| Las dependencias no coinciden | Entorno virtual no activado o sin instalar | Activar el `.venv` y ejecutar `pip install -r requirements.txt`. |
| Los tiempos de `timeit` difieren de los del informe | Las mediciones dependen del hardware | Es esperable; la jerarquía de complejidad (O(n²) > O(n log n)) se mantiene en cualquier máquina. |

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
Para complementar la trazabilidad metodológica de esta fase, las decisiones técnicas del pipeline se documentan en `docs/decisiones_tecnicas_pipeline.md`. En dicho archivo se justifican las principales transformaciones aplicadas, incluyendo la imputación de valores faltantes, la codificación de variables categóricas, la creación de variables derivadas, la normalización con `MinMaxScaler` y las validaciones implementadas sobre el dataset procesado.

---

## Fase 3 — Algoritmos, POO y mediciones de complejidad

En la Fase 3 se encapsuló el pipeline de la Fase 2 en una clase Python orientada a objetos y se implementaron algoritmos estructurados y recursivos sobre el dataset, midiendo su complejidad temporal y espacial.

### Clase `Preprocesador` (`src/Preprocesador.py`)

| Método | Responsabilidad |
|---|---|
| `cargar_datos()` | Carga el CSV con validación de ruta y tipo |
| `limpiar_datos(df)` | Elimina duplicados e imputa nulos (mediana / moda) |
| `encoding_categorico(df)` | Encoding ordinal para variables con orden; OHE para `Job_Title` |
| `crear_features(df)` | Crea `Skill_Index` y la variable objetivo binaria `High_Risk` |
| `normalizar_datos(df)` | MinMaxScaler sobre variables continuas |
| `validar_datos(df)` | Asserts de integridad (nulos, duplicados, rangos) |
| `pipeline_completo()` | Secuencia completa de los métodos anteriores |
| `exportar_dataset(df, path)` | Exporta el dataset procesado a CSV |

### Algoritmos implementados (`notebooks/F3_Definicion.ipynb`)

| Algoritmo | Complejidad | Tipo | Aplicación |
|---|---|---|---|
| Bucle fila a fila vs. vectorización pandas | O(n·k) ambas | Iterativo | Cálculo de `Skill_Index` |
| Bubble Sort | O(n²) tiempo, O(1) espacio | Iterativo | Ordenamiento de referencia |
| Merge Sort | O(n log n) tiempo, O(n) espacio | **Recursivo** | Ordenamiento y ranking de riesgo |
| pandas `sort_values()` | O(n log n) — Tim Sort | Interno (C) | Ordenamiento optimizado |
| Búsqueda binaria | O(log n) tiempo, O(log n) espacio | **Recursivo** | Segmentación por umbral de riesgo |

### Criterios de optimización aplicados

- **Vectorización sobre bucles:** las operaciones pandas delegan a NumPy (C compilado), eliminando el overhead del intérprete Python. Medición con `timeit` demuestra aceleraciones de 50–200× sobre bucles equivalentes.
- **Merge Sort vs. Bubble Sort:** Merge Sort O(n log n) supera a Bubble Sort O(n²) en datasets de tamaño moderado (n ≈ 5 000). La diferencia se amplifica con n creciente.
- **Búsqueda binaria vs. lineal:** requiere ⌈log₂ n⌉ comparaciones en lugar de n; aplicable cuando los datos están ordenados.
- **Complejidad espacial:** Bubble Sort usa O(1) espacio extra (in-place); Merge Sort usa O(n) (sublistas). Medido con `tracemalloc`.

---

## Integrantes

- Arturo Knopke Vera  
- Nicolás Soletic Cobos  
- Roberto Moncada González
- Sebastián Navarrete Soto  

**Docente:** Omar Salinas Silva  
**Curso:** MCDI500 — Herramientas de Software Científico  
**Universidad Andrés Bello — Magíster en Ciencia de Datos e Inteligencia Artificial**


