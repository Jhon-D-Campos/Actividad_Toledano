from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from src.config import NUM_FEATURES, CAT_FEATURES, GEO_FEATURES

def build_preprocessor() -> ColumnTransformer:
    """
    Función que imputa valores faltantes, escala columnas numéricas y codigica columnas categóricas.

    Returns: ColumnTransformer. Objeto que condensa el flujo (preprocesamiento)
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

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', num_pipeline, GEO_FEATURES + NUM_FEATURES),
            ('cat', cat_pipeline, CAT_FEATURES)
        ],
        remainder='drop'
    )

    return preprocessor