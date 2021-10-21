from . import downloadFromURL as durl
import pandas as pd
from pathlib import Path

datasets_path = "C:/Users/Sugato/STUDIES/Hands_on_ML/datasets"

def load_housing_data() :
    housing_path = Path(datasets_path) / "housing"
    durl.fetch_housing_data()
    csv_path = housing_path / "housing.csv"
    return pd.read_csv(csv_path)
    
# for testing purpose
# housing = load_housing_data()
# print(housing.head())





