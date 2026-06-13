# Fase 3 — Núcleo algorítmico, POO y mediciones de complejidad

## Entregables de esta fase

| Artefacto | Ubicación | Descripción |
|---|---|---|
| Notebook ejecutable | `notebooks/F3_Definicion.ipynb` | Flujo completo: preprocesamiento F2, algoritmos, POO, mediciones |
| Módulo POO | `src/transformadores.py` | Jerarquía `Transformador` (ABC) → subclases + clase `Pipeline` |
| Módulo algoritmos | `src/algoritmos.py` | `merge_sort`, `busqueda_binaria`, `bubble_sort` recursivos/iterativos |
| Clase Preprocesador | `src/Preprocesador.py` | Pipeline completo de F2 encapsulado en POO |

## Cómo ejecutar

```bash
# Desde la raíz del repositorio:
source .venv/bin/activate
jupyter lab
# Abrir notebooks/F3_Definicion.ipynb → Kernel → Restart & Run All
```

## Lo nuevo respecto a la Fase 2

- `src/transformadores.py` — herencia (`ImputarMediana`, `ImputarModa`, `EscalarMinMax`, `EscalarZScore` heredan de `Transformador`) y polimorfismo (`Pipeline.ejecutar()` llama `aplicar()` sin conocer la clase concreta).
- `src/algoritmos.py` — algoritmos recursivos (`merge_sort` O(n log n), `busqueda_binaria` O(log n)) con mediciones de complejidad temporal y espacial vía `timeit` y `tracemalloc`.
