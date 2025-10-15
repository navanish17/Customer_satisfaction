from pathlib import Path
import sys
from pipeline.training_pipeline import train_pipeline


def main(data_path: str):
    """Run the training pipeline with the provided data path.

    This validates the path and then invokes the ZenML pipeline function.
    """
    path = Path(data_path)
    if not path.exists():
        print(f"Data file not found: {path}")
        sys.exit(1)

    # call the pipeline (ZenML pipeline decorated function)
    pipeline_run = train_pipeline(str(path))
    try:
        # If ZenML requires .run(), call it. If train_pipeline is configured to run
        # immediately, this will still be fine. We attempt to call .run() if available.
        run_method = getattr(pipeline_run, "run", None)
        if callable(run_method):
            run_method()
        else:
            # If the decorator returned a callable that triggers execution, call it
            if callable(pipeline_run):
                pipeline_run()
    except Exception as e:
        print(f"Error running pipeline: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Use a relative path from the repository root by default
    default = Path(__file__).resolve().parent / "Data" / "olist_customers_dataset.csv"
    main(default)