"""
Script Principal de Entrenamiento y Selección de Modelos.
Coordinación del Flujo: Carga -> Preprocesamiento -> Entrenamiento -> Selección -> Evaluación Final.
Autor: Jhonatan Díaz
"""

from src.io import Dataset
from src.evaluation import ModelEvaluation
from src.preprocessor import build_preprocessor

from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor


def train():
    print("=" * 65)
    print("INICIANDO PIPELINE DE MACHINE LEARNING")
    print("=" * 65)

    # 1. Carga de Datos
    print("\n[1/3] Cargando conjunto de datos...")
    data = Dataset(seed=43, num_samples=None)
    X_train, y_train = data.load_xy()
    print(f"  Datos cargados: {X_train.shape[0]} muestras.")

    # 2. Diccionario de Modelos a Evaluar
    models_to_test = {
        "Linear Regression": LinearRegression(),
        "Decision Tree": DecisionTreeRegressor(random_state=43),
        "Random Forest": RandomForestRegressor(random_state=43),
        "KNN Regressor": KNeighborsRegressor()
    }

    best_model_name = None
    best_r2_score = float("-inf")
    best_pipeline = None

    print("\n[2/3] Entrenando y evaluando candidatos en Validación...")
    ev = ModelEvaluation(X=X_train, y=y_train)

    # 3. Iterar, Entrenar y Seleccionar el Mejor
    for name, model in models_to_test.items():
        print(f"\n   Evaluando: {name}...")
        
        # Construir Pipeline: Preprocesador + Modelo
        pipeline = Pipeline([
            ("preprocessor", build_preprocessor()),
            ("model", model)
        ])
        
        # Evaluar
        metrics = ev.evaluate_model(model=pipeline)
        
        # Extraer R2 de manera segura (probando claves en mayúsculas o minúsculas)
        r2 = 0
        if isinstance(metrics, dict):
            r2 = metrics.get("R2", metrics.get("r2", metrics.get("r2_score", 0)))
        
        # Criterio de selección: Mayor R2
        if r2 > best_r2_score:
            best_r2_score = r2
            best_model_name = name
            best_pipeline = pipeline

    # 4. Resultado Final
    print("\n" + "=" * 65)
    print(f"MEJOR MODELO SELECCIONADO: {best_model_name.upper() if best_model_name else 'NINGUNO'}")
    print(f"   R² alcanzado: {best_r2_score:.4f}")
    print("=" * 65)
    print("\n¡Pipeline completado con éxito!")

    return best_pipeline


if __name__ == "__main__":
    train()