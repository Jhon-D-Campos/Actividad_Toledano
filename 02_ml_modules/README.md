#  Proyecto de Machine Learning: Predicción de Viviendas

Este repositorio contiene la reestructuración modular de un flujo de Machine Learning para predecir el valor medio de las viviendas (`median_house_value`), pasando de un entorno exploratorio (Marimo notebook) a una arquitectura limpia, profesional y ejecutable en Python.

---

##  Equipo y Tabla de Contribuciones

| Integrante | Usuario GitHub | Módulos a Cargo | Contribución Realizada |
| :--- | :--- | :--- | :--- |
| **Jhonatan Díaz** | `@Jhon-D-Campos` | `train.py`, `requirements.txt`, `.gitignore`, `README.md` | Orquestación del flujo principal (`train.py`), configuración del entorno, gestión de Git y documentación base. |
| **Adrian Camacho** | `@camachojaja` | `src/config.py`, `src/io.py` | Definición de rutas y semillas globales, y creación del módulo de carga de datos desde CSV. |
| **Elías Sierra** | `@issierra` | `src/preprocessor.py` | Identificación de tipos de columnas y construcción de Pipelines de preprocesamiento (evitando data leakage). |
| **Yuli Gutiérrez** | `@yuligutierrez0198-lang` | `src/models.py`, `src/evaluation.py` | Configuración e integración de modelos de ML en Pipelines de Scikit-Learn y métricas de evaluación ($R^2$, RMSE, MAE). |

---

##  Organización del Repositorio

```text
02_ml_modules/
│── src/
│   ├── config.py          # Configuración global (semillas, rutas, variables)
│   ├── io.py              # Módulo de carga de datos desde CSV
│   ├── preprocessor.py    # Pipeline de preprocesamiento (StandardScaler, OneHotEncoder)
│   ├── models.py          # Definición de arquitecturas de modelos
│   └── evaluation.py      # Clase de evaluación y cálculo de métricas
│── .gitignore             # Exclusión de archivos basura y temporales
│── README.md              # Documentación principal del proyecto
│── requirements.txt       # Dependencias del proyecto
└── train.py               # Script principal de orquestación y selección de modelo