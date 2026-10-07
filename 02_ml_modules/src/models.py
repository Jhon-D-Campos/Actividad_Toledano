# src/models.py
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

import sys
from pathlib import Path

# Añade la carpeta 'src' al path de Python
sys.path.append(str(Path(__file__).resolve().parent))

from preprocessor import build_preprocessor

def build_pipeline(model_name: str = "random_forest") -> Pipeline:
    """
    Integra el preprocesador y el modelo de ML en un Pipeline de Scikit-Learn.
    """
    preprocessor = build_preprocessor()

    # Selección de al menos 2 modelos distintos
    if model_name == "random_forest":
        model = RandomForestRegressor(random_state=42)
    elif model_name == "linear_regression":
        model = LinearRegression()
    elif model_name == "decision_tree":
        model = DecisionTreeRegressor(random_state=42)
    else:
        raise ValueError(f"Modelo '{model_name}' no soportado.")

    # Integración en Pipeline
    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", model)
        ]
    )

    return pipeline