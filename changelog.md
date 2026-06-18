# Changelog — Impacto de la IA en el Empleo (Hacia 2030)

Registro de cambios significativos por fase. Formato inspirado en [Keep a Changelog](https://keepachangelog.com/).

---

## [F4 — Revisión] — 2026-06-17

### Commits de esta revisión (rama f4_s4_etapa4)
- `ba82760` — docs: registro de cambios en esta fase
- `da2d841` — feat: se incorporan graficas candidatas
- `5b2764d` — docs: se actualiza el readme
- `35402f1` — docs: graficos generados del notebook
- `09db74c` — docs: actualiza bibliografía del notebook

### Fixed
- Afirmaciones analíticas no respaldadas por datos:
  - Acto 2: el boxplot mostraba medianas casi iguales (0.49–0.52, Δ=0.03) pero el texto afirmaba "factor protector". Corregido.
  - Acto 3: correlaciones salario/exposición ≈ 0; eliminadas anotaciones "zona de potenciación/sustitución". Corregido.
- Caso límite de validación: ahora introduce un NaN real y verifica `ImputarMediana.aplicar()`.
- Complejidad espacial de Bubble Sort: O(1) → O(n) por copia defensiva (`arr = list(arr)`).
- Referencia no verificable "foro técnico de la Semana 1" eliminada; sustituida por cita APA 7.
- Afirmación "todos los empleos requieren adaptación" eliminada (no respaldada por los datos).

### Added
- Reestructuración del storytelling: Acto 3 = riesgo por ocupación (resultado bipolar: 5 ocupaciones > 98 %, 15 con 0 %); scatter plot relegado a V.d suplementario.
- Citas APA 7 integradas en el texto del notebook (II.b, II.e, V, VIII).
- Factor de aceleración corregido: "≈146×" → "más de 140×" (medición real ≈ 143×).
- `docs/viz_acto3_suplementario.png`: gráfico suplementario salario × exposición IA.
- Índice actualizado con V.d.
- Trazabilidad de mejoras ampliada con filas de revisión F4.
- Módulos heredados (`features.py`, `modeling.py`, `evaluation.py`) documentados en III.b.

### Changed
- `Readme.md`: Python 3.12.10 → 3.12.13; Bubble Sort O(1) → O(n); descripciones de Acto 2 y 3.
- `src/algoritmos.py`: docstring de `bubble_sort` corregido a O(n) espacio.

### Impact
- Veracidad estadística de todas las afirmaciones analíticas.
- Historia coherente con los datos reales (storytelling: contexto → conflicto → resolución con ocupación).
- Código de validación técnica realmente ejercita las funciones del proyecto.

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
- `docs/viz_acto3_resolucion.png`: gráfico 3 — riesgo de automatización por tipo de ocupación.
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
