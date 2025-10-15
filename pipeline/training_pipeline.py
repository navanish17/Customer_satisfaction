from typing import Any
from zenml import pipeline
from Steps.model_train import model_training
from Steps.ingest_data import ingestdata
from Steps.clean_data import clean_df
from Steps.evaluation import evaluation_df


@pipeline
def train_pipeline(data_path: str) -> Any:
    """Assemble the ZenML training pipeline.
    Args:
        data_path: path to the input CSV file.
    Returns:
        The pipeline object or run result returned by the ZenML decorator.
    """
    df = ingestdata(data_path)
    cleaned = clean_df(df)
    model_trained = model_training(cleaned) 
    evaluation_df(model_trained)

    # The decorated function typically returns a pipeline object; let the
    # ZenML decorator handle and return it.