import logging
import pandas as pd
from zenml import step

class Ingest_data:
    def __init__(self, datapath:str):
        self.datapath = datapath
    
    def get_data(self):
        logging.info(f"Data has been ingested from {self.datapath}")
        return pd.read_csv(self.datapath)

@step

def ingestdata(data_path:str)-> pd.DataFrame:
    """ 
    This function will initiate the class to ingest the data 
    """
    try:
        ingestor  = Ingest_data(data_path)
        df = ingestor.get_data()
        return df
    except Exception as e:
        logging.error(f"error has been ocured while data ingeston i.e {e}")
        raise e
        