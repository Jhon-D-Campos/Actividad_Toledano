# Predicción del Valor de Viviendas con Machine Learning

Este repositorio contiene la reestructuración modular de un flujo de Machine Learning para predecir el valor medio de las viviendas (`median_house_value`), pasando de un entorno exploratorio (Marimo notebook) a una arquitectura limpia, profesional y ejecutable en Python.

---

## Equipo y Tabla de Contribuciones

| **Integrante**     | **Usuario GitHub**        | **Módulos a Cargo**                                       | **Contribución Realizada**                                                                                                          | **Commit**                      |
| ------------------ | ------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| **Jhonatan Díaz**  | `@Jhon-D-Campos`          | `train.py`, `requirements.txt`, `.gitignore`, `README.md` | Orquestación del flujo principal (`train.py`), configuración del entorno, gestión de Git y documentación del proyecto.              | `ed3d4f2`, `a13d0da` |
| **Adrian Camacho** | `@camachojaja`            | `src/config.py`, `src/io.py`                              | Definición de rutas y semillas globales, y creación del módulo de carga de datos desde CSV.                                         | `7dd012b` `1cdcd7b`                      |
| **Elías Sierra**   | `@issierra`               | `src/preprocessor.py`                                     | Identificación de tipos de columnas y construcción de Pipelines de preprocesamiento, evitando problemas de *data leakage*.          | `61eba02`                       |
| **Yuli Gutiérrez** | `@yuligutierrez0198-lang` | `src/models.py`, `src/evaluation.py`                      | Configuración e integración de modelos de Machine Learning en Pipelines de Scikit-Learn y métricas de evaluación (`R2`, RMSE, MAE). | `d02708c`                       |

> **Nota:** Los identificadores corresponden a los commits del historial de Git utilizados como evidencia de las contribuciones realizadas por cada integrante.

---

## Organización del Repositorio

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

## Resultados e Interpretación

Se evaluaron 4 algoritmos de regresión distintos bajo las mismas condiciones de preprocesamiento y partición de datos:

| **Modelo**                  | **R2 Score** |       **RMSE** |        **MAE** |
| --------------------------- | -----------: | -------------: | -------------: |
| **Random Forest (Ganador)** |     **0.81** | **$50,620.93** | **$33,074.06** |
| KNN Regressor               |         0.72 |     $61,681.06 |     $41,459.27 |
| Linear Regression           |         0.66 |     $68,114.96 |     $49,542.34 |
| Decision Tree               |         0.63 |     $70,365.35 |     $45,232.32 |

### Interpretación

El modelo de **Random Forest** demostró la mayor capacidad explicativa, logrando un `R2` de **0.81**, superando por un margen amplio a los modelos lineales y basados en distancias.

Esto indica que el modelo logra explicar aproximadamente el **81 % de la variabilidad** observada en el valor medio de las viviendas dentro del conjunto de datos utilizado.

---

## Limitaciones Conocidas

* **Costo computacional:** El tiempo de entrenamiento de Random Forest puede incrementarse al aumentar el número de estimadores o la cantidad de datos.
* **Sin optimización de hiperparámetros:** Los modelos fueron evaluados con sus configuraciones por defecto. Un ajuste mediante `GridSearchCV` podría mejorar los resultados.
* **Dependencia de las características disponibles:** La capacidad predictiva está limitada por las variables presentes en el conjunto de datos.

---

## Instrucciones de Ejecución

### 1. Instalar dependencias

Desde la terminal, dentro de la carpeta del proyecto:

```bash
pip install -r requirements.txt
```

### 2. Ejecutar el pipeline de entrenamiento

```bash
python train.py
```

El script se encarga de cargar los datos, realizar el preprocesamiento, entrenar los modelos candidatos, calcular las métricas de evaluación y seleccionar el modelo con el mejor rendimiento.

---

## Reflexiones Finales del Equipo

### ¿Qué implementaste y qué decisión técnica tomaste?

Implementamos el script orquestador `train.py`, `.gitignore` y `requirements.txt`. Decidimos iterar dinámicamente sobre los modelos candidatos construyendo Pipelines con `build_preprocessor()` de Scikit-Learn para comparar las métricas en tiempo de ejecución y seleccionar automáticamente al ganador en función del `R2`.

### ¿Cómo verificaste tu aportación?

Ejecutamos:

```bash
python train.py
```

en la terminal, verificando la carga correcta de los datos, el correcto funcionamiento del preprocesamiento, la ausencia de fuga de datos (*data leakage*) y la selección automática del modelo con el rendimiento más alto: **Random Forest con `R2 ≈ 0.81`**.

### ¿Qué observaste o aprendiste al revisar el trabajo de otra persona?

Aprendimos la importancia de estandarizar los valores de retorno entre módulos, como asegurar que el método de evaluación retorne un diccionario con las métricas correspondientes. Esto permite una integración más limpia entre los diferentes componentes del proyecto y evita errores durante la ejecución.

### ¿Qué mejorarías en la siguiente versión?

Como equipo, consideramos que una siguiente versión podría incorporar un módulo de persistencia para exportar el mejor modelo entrenado a un archivo `.joblib` o `.pkl`. También sería conveniente implementar una etapa de búsqueda y optimización de hiperparámetros mediante `GridSearchCV` para intentar mejorar el rendimiento de los modelos.

---

## Repositorio

**Repositorio del proyecto:**
[Agregar aquí el enlace al repositorio de GitHub]

---

## Identificadores de los Commits

Como evidencia de las contribuciones individuales, se identificaron los siguientes commits en el historial del repositorio:

* **Jhonatan Díaz:** `ed3d4f2`, `a13d0da`, `1cdcd7b`
* **Adrian Camacho:** `7dd012b`
* **Elías Sierra:** `61eba02`
* **Yuli Gutiérrez:** `d02708c`
