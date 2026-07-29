import pandas as pd
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler

def load_data(path):
    return pd.read_csv(path)

def basic_cleaning(df):
    df = df.drop_duplicates()
    df = df.dropna()
    return df

def preprocess_features(df):
    categorical_cols = ['Gender', 'University', 'Degree Programme']
    numeric_cols = ['Academic Workload',
                    'Assignment Frequency',
                    'Self-study Hours',
                    'Part-time Working Hours',
                    'Attendance Percentage',
                    'Previous Semester GPA']

    df = pd.get_dummies(df, columns=categorical_cols)

    scaler = MinMaxScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    return df
