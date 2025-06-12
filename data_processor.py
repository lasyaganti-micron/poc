import pandas as pd

def generate_summary(df):
    return df.describe()

def custom_analysis(df):
    return df[df.columns[0]].value_counts()
