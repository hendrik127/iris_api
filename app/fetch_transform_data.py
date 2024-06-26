"""

Data Processing Functions for Iris Dataset

This module provides functions to fetch, process, and transform iris dataset
data stored in CSV format. It includes functions for fetching data from a URL
specified in environment variables, marking outliers in the dataset,
transforming the dataset by removing duplicates,
adding ratio columns, marking outliers,
and converting the transformed dataset to JSON format.
"""


import os
from typing import Optional
import pandas as pd
from dotenv import load_dotenv


load_dotenv(os.path.join(os.path.dirname(__file__), '..', 'example.env'))


def fetch_iris_data() -> pd.DataFrame:
    """Fetches iris data from a given source URL specified in the environment variables.

    Returns:
        pd.DataFrame: DataFrame containing the iris data if available, otherwise None.
    """
    url = os.getenv("DATA_URL")
    dataframe = pd.read_csv(url)
    return dataframe


def mark_outliers(df: pd.DataFrame) -> pd.DataFrame:
    """Marks outliers in the given DataFrame.

    An outlier is defined as a value that is outside 0.5 times the 
    interquartile range (IQR) above the 75th percentile or below the
    25th percentile for each numeric column.

    Args:
        df (pd.DataFrame): DataFrame containing the iris data.

    Returns:
        pd.DataFrame: DataFrame with an added 'is_outlier'
        column where True indicates an outlier.
    """
    numeric_cols = df.select_dtypes(include='number').columns
    for column in numeric_cols:
        if column == 'is_outlier':
            continue
        # Calculate Q1 (25th percentile) and Q3 (75th percentile)
        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)
        # Calculate the Interquartile Range (IQR)
        iqr = q3 - q1
        c = 0.5
        # Determine the lower and upper bounds for outliers
        lower_bound = q1 - c * iqr
        upper_bound = q3 + c * iqr
        # Mark the rows that are outliers
        outliers_mask = (df[column] < lower_bound) | (df[column] > upper_bound)
        df.loc[outliers_mask, 'is_outlier'] = True
        df.loc[~outliers_mask, 'is_outlier'] = False
    return df


def transform_iris_data(df: pd.DataFrame) -> Optional[str]:
    """Transforms the iris DataFrame by removing duplicates,
      adding ratio columns, marking outliers, and resetting the index.

    Args:
        df (pd.DataFrame): DataFrame containing the iris data.

    Returns:
        Optional[str]: JSON string representation of the transformed DataFrame.
    """
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
    """
    This function combines fetch_iris_data and transform_iris_data.

    Returns:
        Optional[str]: JSON string representation of the transformed iris data.
    """
    return transform_iris_data(fetch_iris_data())
