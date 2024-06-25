import pandas as pd
from typing import Optional
from dotenv import load_dotenv
import os


load_dotenv(os.path.join(os.path.dirname(__file__), '..', 'example.env'))


def fetch_iris_data() -> pd.DataFrame:
    """Fetches iris data from given source.
    Returns:
        pd.DataFrame: Dataframe if data available,
        otherwise None.
    """
    url = os.getenv("DATA_URL")
    dataframe = pd.read_csv(url)
    return dataframe


def mark_outliers(df: pd.DataFrame) -> pd.DataFrame:
    numeric_cols = df.select_dtypes(include='number').columns
    for column in numeric_cols:
        if column == 'is_outlier':
            continue
        # Calculate Q1 (25th percentile) and Q3 (75th percentile)
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        # Calculate the Interquartile Range (IQR)
        IQR = Q3 - Q1
        c = 0.5
        # Determine the lower and upper bounds for outliers
        lower_bound = Q1 - c * IQR
        upper_bound = Q3 + c * IQR
        # Mark the rows that are outliers
        outliers_mask = (df[column] < lower_bound) | (df[column] > upper_bound)
        df.loc[outliers_mask, 'is_outlier'] = True
        df.loc[~outliers_mask, 'is_outlier'] = False
    return df


def transform_iris_data(df: pd.DataFrame) -> Optional[str]:
    # Remove duplicates.
    df.drop_duplicates(inplace=True)
    # Add columns for the ratios
    df['sepal_ratio'] = df['sepal_width'] / df['sepal_length']
    df['petal_ratio'] = df['petal_width'] / df['petal_length']
    # Mark outliers.
    df = mark_outliers(df)
    # Replace index with id
    df = df.reset_index().rename(columns={'index': 'id'})
    df['id'] = df['id'] + 1
    return df.to_json(orient='records')


def fetch_and_transform_iris_data():
    return transform_iris_data(fetch_iris_data())
