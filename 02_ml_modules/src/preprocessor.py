from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from src.config import NUM_FEATURES, CAT_FEATURES, GEO_FEATURES

def build_preprocessor() -> ColumnTransformer:
    """
    Función que escala columnas numéricas y codifica columnas categóricas,

    Returns: ColumnTransformer. Objeto que condensa el flujo (preprocesamiento)
    de los datos de entrada.

    """

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', MinMaxScaler(), GEO_FEATURES + NUM_FEATURES),
            ('cat', OneHotEncoder(handle_unknown="ignore"), CAT_FEATURES)
        ],
        remainder='drop'
    )

    return preprocessor