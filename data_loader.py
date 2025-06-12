import pandas as pd
import os

DATA_DIR = "data"

def get_excel_files():
    return [os.path.join(DATA_DIR, f) for f in os.listdir(DATA_DIR) if f.endswith('.xlsx')]

def load_data(file_path):
    return pd.read_excel(file_path, engine="openpyxl")

def save_data(file_path, df):
    df.to_excel(file_path, index=False, engine="openpyxl")
