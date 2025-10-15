import logging
from typing import*
from zenml import step
import pandas as pd


@step
def evaluation_df(df: pd.DataFrame) -> Annotated[pd.DataFrame, "Evaluation"]:
    """Evaluate the trained model or predictions."""
    # Bas ek sample evaluation logic
    logging.info("Running evaluation on DataFrame")

    # For example: describe statistics as evaluation
    evaluation = df.describe()

    # Zaroori hai return karna (DataFrame type)
    return evaluation

    