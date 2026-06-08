# Decisiones técnicas del pipeline de preprocesamiento — Fase 2

## Dataset: AI Impact on Jobs 2030

---

## 1. Encoding de variables categóricas

### 1.1 `Job_Title` — One-Hot Encoding (OHE)

**Tipo de variable:** categórica nominal (sin orden entre categorías).  
**Decisión:** OHE con `pd.get_dummies()`.  
**Justificación:** Las 20 ocupaciones (Software Engineer, Nurse, Doctor, etc.) no tienen relación de orden entre sí. Asignar valores enteros secuenciales (Label Encoding) introduciría una jerarquía artificial que no existe en los datos (e.g., Doctor=5 > Nurse=3 no significa nada). OHE representa cada categoría como una variable binaria independiente, preservando la equidistancia entre categorías.  
**Resultado:** 20 columnas `Job_Title_*` tipo booleano.

### 1.2 `Education_Level` — Encoding ordinal con mapeo explícito

**Tipo de variable:** categórica ordinal (con orden implícito).  
**Decisión:** mapeo directo `{'High School': 0, "Bachelor's": 1, "Master's": 2, 'PhD': 3}`.  
**Justificación:** Existe un orden lógico y convencional entre niveles educativos. Preservar ese orden permite a los algoritmos de ML explotar la relación jerárquica. OHE perdería esa información de orden, y LabelEncoder sin mapeo explícito podría asignar un orden arbitrario (e.g., Bachelor's=0, High School=1).  
**Resultado:** columna int con valores 0, 1, 2, 3.

### 1.3 `Risk_Category` — Encoding ordinal con mapeo explícito

**Tipo de variable:** categórica ordinal.  
**Decisión:** mapeo directo `{'Low': 0, 'Medium': 1, 'High': 2}`.  
**Justificación:** Low < Medium < High es una jerarquía de riesgo semánticamente significativa. Preservar ese orden es esencial para modelos que aprenden relaciones monotónicas entre el nivel de riesgo y otras variables.  
**Resultado:** columna int con valores 0, 1, 2.

---

## 2. Feature Engineering

### 2.1 `Skill_Index`

**Definición:** promedio de las columnas `Skill_1` a `Skill_10`.  
**Justificación:** Las 10 columnas de habilidades representan distintas dimensiones de competencia laboral. Un índice agregado permite capturar el perfil general de habilidades de una ocupación con una sola variable, reduciendo la dimensionalidad sin perder información clave.  
**Rango:** [0, 1] (heredado de las columnas de skills, ya normalizadas en origen).

### 2.2 `High_Risk` (variable objetivo)

**Definición:** `Automation_Probability_2030 > 0.7` → 1; en caso contrario → 0.  
**Justificación:** El umbral de 0.7 (70% de probabilidad de automatización) se adopta como criterio de clasificación de riesgo alto, consistente con la literatura sobre transformación laboral por IA. Permite formular el problema como clasificación binaria supervisada.  
**Distribución esperada:** desbalanceada (pocas ocupaciones superan el umbral).

---

## 3. Normalización

**Método:** `MinMaxScaler` de scikit-learn, escala al rango [0, 1].  
**Columnas normalizadas:** `Average_Salary`, `Years_Experience`, `Tech_Growth_Factor`, `Education_Level`, `Risk_Category`.  
**Justificación:** Variables como `Average_Salary` (rango ~30.000–150.000) y `Years_Experience` (0–30) tienen escalas muy distintas a `AI_Exposure_Index` (0–1). Sin normalización, los algoritmos basados en distancias (k-NN, SVM, redes neuronales) darían peso desproporcionado a variables de mayor escala. MinMaxScaler se eligió sobre StandardScaler porque el dataset no tiene outliers extremos y se quiere mantener el rango acotado.

---

## 4. Limpieza

- **Duplicados:** eliminados con `drop_duplicates()`.
- **Nulos numéricos:** imputados con la mediana de cada columna.
- **Nulos categóricos:** imputados con la moda de cada columna.
- **Nota:** el dataset original `AI_Impact_on_Jobs_2030.csv` no contiene nulos ni duplicados, pero el pipeline aplica limpieza de forma defensiva para garantizar reproducibilidad ante futuras versiones del dataset.

---

## 5. Validaciones aplicadas

| Validación | Criterio |
|---|---|
| Sin nulos | `df.isnull().sum().sum() == 0` |
| Sin duplicados | `df.duplicated().sum() == 0` |
| DataFrame no vacío | `len(df) > 0` |
| `AI_Exposure_Index` en [0,1] | `between(0, 1).all()` |
| `Automation_Probability_2030` en [0,1] | `between(0, 1).all()` |
| `High_Risk` solo 0 o 1 | `isin([0, 1]).all()` |
| `Education_Level` en [0,1] post-norm. | `between(0, 1).all()` |
| `Risk_Category` en [0,1] post-norm. | `between(0, 1).all()` |
