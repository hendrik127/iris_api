import pandas as pd
from typing import Optional
from dotenv import load_dotenv
import os


load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))


def fetch_iris_data() -> Optional[str]:
    """Converts data from given source to a JSON string.
    Returns:
        Optional[str]: The JSON string of the data if available,
        otherwise None.
    """
    url = os.getenv("DATA_SOURCE_API")
    df = pd.read_csv(url)
    df = df.reset_index().rename(columns={'index': 'id'})
    df['id'] = df['id'] + 1
    return df.to_json(orient='records')
