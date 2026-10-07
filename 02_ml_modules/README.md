#  Proyecto de Machine Learning: Predicción de Viviendas

Este repositorio contiene la reestructuración modular de un flujo de Machine Learning para predecir el valor medio de las viviendas (`median_house_value`), pasando de un entorno exploratorio (Marimo notebook) a una arquitectura limpia, profesional y ejecutable en Python.

---

##  Equipo y Tabla de Contribuciones

| Integrante         | Usuario GitHub            | Módulos a Cargo                                           | Contribución Realizada                                                                                                 |
| :----------------- | :------------------------ | :-------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------- |
| **Jhonatan Díaz**  | `@Jhon-D-Campos`          | `train.py`, `requirements.txt`, `.gitignore`, `README.md` | Orquestación del flujo principal (`train.py`), configuración del entorno, gestión de Git y documentación base.         |
| **Adrian Camacho** | `@camachojaja`            | `src/config.py`, `src/io.py`                              | Definición de rutas y semillas globales, y creación del módulo de carga de datos desde CSV.                            |
| **Elías Sierra**   | `@issierra`               | `src/preprocessor.py`                                     | Identificación de tipos de columnas y construcción de Pipelines de preprocesamiento (evitando data leakage).           |
| **Yuli Gutiérrez** | `@yuligutierrez0198-lang` | `src/models.py`, `src/evaluation.py`                      | Configuración e integración de modelos de ML en Pipelines de Scikit-Learn y métricas de evaluación ($R^2$, RMSE, MAE). |

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
```

---

##  Resultados e Interpretación

Se evaluaron 4 algoritmos de regresión distintos bajo las mismas condiciones de preprocesamiento y partición de datos:

| **Modelo**                  | **R2 Score** | **RMSE**       | **MAE**        |
| --------------------------- | ------------ | -------------- | -------------- |
| **Random Forest** (Ganador) | **0.81**     | **$50,620.93** | **$33,074.06** |
| KNN Regressor               | 0.72         | $61,681.06     | $41,459.27     |
| Linear Regression           | 0.66         | $68,114.96     | $49,542.34     |
| Decision Tree               | 0.63         | $70,365.35     | $45,232.32     |

**Interpretación:** El modelo de **Random Forest** demostró la mayor capacidad explicativa, logrando un $R^2$ de **0.81**, superando por un margen amplio a los modelos lineales y basados en distancias.

---

##  Limitaciones Conocidas

* **Costo computacional:** El tiempo de entrenamiento de Random Forest se incrementa linearmente al aumentar el número de estimadores o la cantidad de datos.
* **Sin optimización de hiperparámetros:** Los modelos fueron evaluados con sus configuraciones por defecto; un ajuste mediante `GridSearchCV` podría mejorar los resultados.

---

##  Instrucciones de Ejecución

### 1. Instalar dependencias

Bash

```bash
pip install -r requirements.txt
```

### 2. Ejecutar el pipeline de entrenamiento

Bash

```bash
python train.py
```

---

##  Reflexiones Finales del Equipo


* **¿Qué implementaste y qué decisión técnica tomaste?**

  Implementamos el script orquestador `train.py`, `.gitignore` y `requirements.txt`. Decidimos iterar dinámicamente sobre los modelos candidatos construyendo pipelines con `build_preprocessor()` de Scikit-Learn para comparar métricas en tiempo de ejecución y seleccionar automáticamente al ganador en base al $R^2$.

* **¿Cómo verificaste tu aportación?**

  Ejecutamos `python train.py` en la terminal verificando la carga correcta de datos, la ausencia de fuga de datos (*data leakage*) y la selección automática del modelo con el rendimiento más alto (**Random Forest** con $R^2 \approx 0.81$).

* **¿Qué observaste o aprendiste al revisar el trabajo de otra persona?**

  Aprendimos la importancia de estandarizar los valores de retorno entre módulos (como asegurar que el método de evaluación retorne un diccionario con métricas) para garantizar una integración limpia sin errores de ejecución.

* **¿Qué mejorarías en la siguiente versión?**

  Agregaría un módulo de persistencia para exportar el mejor modelo entrenado a un archivo `.joblib` o `.pkl` y una etapa de búsqueda de hiperparámetros con `GridSearchCV` o al menos es lo que dice la IA que podriamos agregar, aun somos muy inexpertos como para tener el conocimiento de mas amplio.
