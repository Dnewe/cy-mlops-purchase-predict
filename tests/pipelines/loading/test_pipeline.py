import pandas as pd
from kedro.runner import SequentialRunner

from purchase_predict.pipelines.loading.pipeline import create_pipeline


def test_pipeline(catalog_test):
    runner = SequentialRunner()
    pipeline = create_pipeline()
    pipeline_output = runner.run(pipeline, catalog_test)
    df = pipeline_output["primary"].load()
    assert type(df) is pd.DataFrame
    assert df.shape[1] == 16
    assert "purchased" in df
