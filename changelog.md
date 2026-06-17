# Changelog — Impacto de la IA en el Empleo (Hacia 2030)

Registro de cambios significativos por fase. Formato inspirado en [Keep a Changelog](https://keepachangelog.com/).

---

## [F4] — 2026-06-16

### Added
- `notebooks/F4_Definicion.ipynb`: notebook integrador final con:
  - Tres visualizaciones analíticas con storytelling (contexto → conflicto → resolución).
  - Secciones de Resultados, Discusión y Conclusiones con contraste de hipótesis.
  - Trazabilidad de mejoras F1–F4 (tabla comparativa y este changelog).
  - Lista de verificación de reproducibilidad.
- `docs/viz_acto1_contexto.png`: gráfico 1 — distribución de categorías de riesgo.
- `docs/viz_acto2_conflicto.png`: gráfico 2 — nivel educativo vs. probabilidad de automatización.
- `docs/viz_acto3_resolucion.png`: gráfico 3 — exposición IA vs. salario coloreado por riesgo.
- `changelog.md`: este archivo de trazabilidad de mejoras.

### Changed
- `Readme.md`: actualizado con sección F4, estructura de repositorio, notebook F4 y tabla de visualizaciones.

### Impact
- Cumple criterios de visualizaciones analíticas, storytelling, resultados, discusión,
  conclusiones y trazabilidad de mejoras (Fase 4).

---

## [F3] — 2026-06-13

### Added
- `src/Preprocesador.py`: clase POO con pipeline completo encapsulado (herencia, polimorfismo,
  encapsulamiento). Métodos: `cargar_datos`, `limpiar_datos`, `encoding_categorico`,
  `crear_features`, `normalizar_datos`, `validar_datos`, `pipeline_completo`, `exportar_dataset`.
- `src/transformadores.py`: jerarquía `Transformador (ABC)` → `ImputarMediana`, `ImputarModa`,
  `EscalarMinMax`, `EscalarZScore` + clase `Pipeline` por composición (patrón Strategy).
- `src/algoritmos.py`: `merge_sort` (O(n log n), recursivo), `merge_sort_key`, `busqueda_binaria`
  (O(log n), recursivo), `bubble_sort` (O(n²), referencia de comparación).
- `notebooks/F3_Definicion.ipynb`: mediciones de complejidad temporal (`timeit`) y espacial
  (`tracemalloc`); comparaciones Big-O; aplicación al dataset real.
- `docs/decisiones_tecnicas_pipeline.md`: justificación de decisiones de diseño.

### Changed
- Pipeline funcional de F2 encapsulado en la clase `Preprocesador`.

### Impact
- Alta cohesión, bajo acoplamiento; pipeline reutilizable vía POO.
- Evidencia cuantitativa de la complejidad algorítmica (Bubble 169 ms/iter vs. Merge 2.2 ms/iter
  vs. pandas 0.1 ms/iter, n=3 000).

---

## [F2] — 2026-06-06

### Added
- `src/preprocessing.py`: funciones atómicas de preprocesamiento:
  - `limpiar_datos`: deduplicación + imputación mediana/moda.
  - `encoding_categorico`: encoding ordinal (`Education_Level`, `Risk_Category`) y OHE (`Job_Title`).
  - `crear_features`: `Skill_Index` (promedio de skills) y `High_Risk` (variable objetivo binaria, umbral 0.7).
  - `normalizar_datos`: MinMaxScaler sobre variables continuas.
  - `validar_datos`: asserts de integridad (nulos, duplicados, rangos).
  - `preprocessing_pipeline`: pipeline completo encadenado.
  - `exportar_dataset`: exportación a `data/processed/`.
- `src/data_loading.py`: función de carga del dataset.
- `data/processed/AI_Impact_on_Jobs_2030_clean.csv`: dataset procesado exportado.
- `notebooks/F2_Definicion.ipynb`: pipeline completo ejecutado y documentado.

### Changed
- Estructura de carpetas del repositorio consolidada (`data/`, `src/`, `notebooks/`, `docs/`).

### Impact
- Dataset procesado reproducible; 3 000 filas × 39 columnas tras encoding y feature engineering.
- Todas las validaciones OK: 0 nulos, 0 duplicados, rangos correctos.

---

## [F1] — 2026-05-30

### Added
- Estructura inicial del repositorio.
- `data/raw/AI_Impact_on_Jobs_2030.csv`: dataset original de Kaggle (3 000 filas × 18 columnas).
- `requirements.txt`: dependencias del entorno virtual.
- `.gitignore`: exclusión de `.venv/`, `__pycache__/`, `.DS_Store`.
- `Readme.md`: descripción inicial del proyecto.

### Impact
- Entorno reproducible configurado; repositorio operativo en GitHub.
