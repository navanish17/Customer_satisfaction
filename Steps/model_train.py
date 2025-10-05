import pandas as pd
import logging
from zenml import step 

@step

def model_train(df:pd.DataFrame) -> None:
    pass