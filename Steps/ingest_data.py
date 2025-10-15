import logging
import pandas as pd
from typing import Annotated
from zenml import step


class Ingest_data:
    def __init__(self, datapath: str):
        self.datapath = datapath
    
    def get_data(self)-> Annotated[pd.DataFrame, "Ingest_data"]:
        logging.info(f"Data has been ingested from {self.datapath}")
        return pd.read_csv(self.datapath)


@step
def ingestdata(data_path: str) -> Annotated[pd.DataFrame, "Ingest_data"]:
    """Initiate an ingestor and return the loaded data.

    Returns Any to avoid Pydantic schema generation for pandas.DataFrame
    when ZenML inspects this function's signature.
    """
    try:
        ingestor = Ingest_data(data_path)
        df = ingestor.get_data()
        return df
    except Exception as e:
        logging.error(f"error has been ocured while data ingeston i.e {e}")
        raise
        