# 🏠 Proyecto de Machine Learning: Predicción de Viviendas

Este repositorio contiene un flujo completo de Machine Learning para la predicción de precios de vivienda (`median_house_value`), implementando una arquitectura modular en Python.

---

## 👥 Equipo y Tabla de Contribuciones

| Integrante | Módulos a Cargo | Contribución Realizada |
| :--- | :--- | :--- |
| **Jhonatan Díaz** | `train.py`, `requirements.txt`, `.gitignore`, `README.md` | Orquestación del flujo principal (`train.py`), configuración del entorno, gestión de Git y documentación base. |
| **Adrian Camacho** | `src/config.py`, `src/io.py` | Definición de rutas y semillas globales, y creación del módulo de carga de datos desde CSV. |
| **Elías Sierra** | `src/preprocessing.py` | Identificación de tipos de columnas y construcción de Pipelines de preprocesamiento (evitando data leakage). |
| **Yuli Gutiérrez** | `src/models.py`, `src/evaluation.py` | Configuración e integración de modelos de ML en Pipelines de Scikit-Learn y métricas de evaluación ($R^2$, RMSE, MAE). |

---

## 🚀 Instrucciones de Ejecución

### 1. Instalar dependencias
```bash
pip install -r requirements.txt