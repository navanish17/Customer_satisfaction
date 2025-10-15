from zenml import pipelines
from Steps.model_train import model_training
from Steps.ingest_data import ingestdata
from Steps.clean_data import clean_df
from Steps.evaluation import evaluation_df

@pipelines
def train_pipeline(datapath:str):
    pass