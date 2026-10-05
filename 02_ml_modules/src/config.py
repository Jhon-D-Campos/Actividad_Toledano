# Configuracion de mis variables utilizadas
from pathlib import Path

# General
SEED = 42

# Path
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "housing.csv"

# Split (Train / Val / Test)
TRAIN_SIZE = 0.70
VAL_SIZE = 0.15
TEST_SIZE = 0.15

# FEATURES

GEO_FEATURES = [
    "longitude",
    "latitude"
]

NUM_FEATURES = [
    "housing_median_age",
    "total_rooms",
    "total_bedrooms",
    "population",
    "households",
    "median_income",
]
CAT_FEATURES = ["ocean_proximity"]

FEATURES =  GEO_FEATURES + NUM_FEATURES + CAT_FEATURES

# TARGET
TARGET = "median_house_value"

# FEATURES DERIVADAS (ingenieria de caracteristicas; se calculan en preprocessor.py)
ENGINEERED_FEATURES = [
    "rooms_per_household",
    "bedrooms_per_room",
    "population_per_household",
]

