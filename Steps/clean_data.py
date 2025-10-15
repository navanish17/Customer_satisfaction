import pandas as pd
import logging
from typing import Annotated
from zenml import step

@step
def clean_df(df: pd.DataFrame) -> Annotated[pd.DataFrame, "clean_df"]: # to prevent pandyatic error also we can return "any"
    """Clean the input DataFrame-like object and return cleaned data.

    Use typing.Any here to avoid Pydantic schema generation for pandas.DataFrame
    when ZenML inspects step function signatures.
    """
    # implement actual cleaning logic in-place. For now, pass-through.
    return df