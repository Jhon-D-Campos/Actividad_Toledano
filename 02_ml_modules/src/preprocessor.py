import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder, FunctionTransformer
from src.config import NUM_FEATURES, CAT_FEATURES, GEO_FEATURES, ENGINEERED_FEATURES

def add_engineered_features(X: pd.DataFrame) -> pd.DataFrame:
    """
    Agrega variables derivadas a partir de las columnas originales.

    Returns: DataFrame con las columnas originales + ENGINEERED_FEATURES.
    """
    X = X.copy()
    X["rooms_per_household"] = X["total_rooms"] / X["households"]
    X["bedrooms_per_room"] = X["total_bedrooms"] / X["total_rooms"]
    X["population_per_household"] = X["population"] / X["households"]
    return X

def build_preprocessor() -> Pipeline:
    """
    Función que imputa valores faltantes, escala columnas numéricas y codifica columnas 
    categóricas.

    Returns: Pipeline. Objeto que condensa el flujo (preprocesamiento)
    de los datos de entrada.
    """

    num_pipeline = Pipeline(
        steps=[
            ("scaler", MinMaxScaler()),
            ("imputer", KNNImputer(n_neighbors=5)),
        ]
    )

    cat_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoder", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    column_transformer = ColumnTransformer(
        transformers=[
            ('num', num_pipeline, GEO_FEATURES + NUM_FEATURES + ENGINEERED_FEATURES),
            ('cat', cat_pipeline, CAT_FEATURES)
        ],
        remainder='drop'
    )

    preprocessor = Pipeline(
        steps=[
            ("feature_engineering", FunctionTransformer(add_engineered_features)),
            ("column_transformer", column_transformer),
        ]
    )

    return preprocessor