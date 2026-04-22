from kedro.io import DataCatalog, MemoryDataset
import pytest


@pytest.fixture(scope="module")
def project_id():
    return "project-a3dc79da-4478-47be-893"


@pytest.fixture(scope="module")
def primary_folder():
    return "cours_mlops/primary/data-test.csv"


@pytest.fixture(scope="module")
def catalog_test(project_id, primary_folder):
    catalog = DataCatalog(
        {
            "params:gcp_project_id": MemoryDataset(project_id),
            "params:gcs_primary_folder": MemoryDataset(primary_folder),
        }
    )
    return catalog
