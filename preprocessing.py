import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_data(file_path):
    
    return pd.read_csv(file_path)

def preprocess(df):  
    df = df.dropna(axis=1, how='all')
    df = df.fillna("Unknown")

   
    for col in df.select_dtypes(include=['object', 'bool']).columns:
        df[col] = LabelEncoder().fit_transform(df[col])

    return df
