import pickle
import sys
import os
import pandas as pd
import numpy as np
import requests
import tarfile

sys.path.append("/home/deepak/practice_git_repo/assignment2/mle-training/")

from src.housing_package.ingest_data import (
    load_housing_data,
)

DOWNLOAD_ROOT = "http://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"


def test_fetch_tgz(housing_url=HOUSING_URL):
    """fetches to the dataset and makes assertion

    Parameters
    ----------

    param1: str
        housing_url: url for fetching the dataset

    Returns
    -----------
    assertion
        True if successful, False otherwise

    """
    tgz_path = os.path.join(os.getcwd(), "housing.tgz")

    r = requests.get(housing_url, timeout=300)
    with open(tgz_path, "wb") as f:
        f.write(r.content)

    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=os.getcwd())
    housing_tgz.close()

    files = os.listdir()
    assert "housing.csv" in files

    column_names = [
        "longitude",
        "latitude",
        "housing_median_age",
        "total_rooms",
        "total_bedrooms",
        "population",
        "households",
        "median_income",
        "median_house_value",
        "ocean_proximity",
    ]
    df = pd.read_csv("housing.csv")
    os.remove("housing.csv")
    assert sorted(df.columns.to_list()) == sorted(column_names)


# def test_lin_reg(MODEL_PATH=MODEL_PATH):
#     """Make model prediction
#     Note: Model should exist in the given path

#     Parameters
#     ----------

#     param1 : str
#         MODEL_PATH: Path of the model

#     Returns
#     -----------
#     assertion
#         True if successful, False otherwise

#     Examples
#     ---------
#     >>> test_lin_reg(MODEL_PATH=MODEL_PATH)
#     assert True

#     """

#     LIN_REG = pickle.load(open(os.path.join(MODEL_PATH, "lin_reg.pkl"), "rb"))
#     arr = np.asarray(
#         [
#             -1.21460000e02,
#             3.85200000e01,
#             2.90000000e01,
#             3.87300000e03,
#             7.97000000e02,
#             2.23700000e03,
#             7.06000000e02,
#             2.17360000e00,
#             5.48583569e00,
#             2.05783630e-01,
#             3.16855524e00,
#             1.00000000e00,
#             0.00000000e00,
#             0.00000000e00,
#             0.00000000e00,
#         ]
#     ).reshape(1, -1)

#     assert round(LIN_REG.predict(arr)[0]) == 85658


# def test_d_tree(MODEL_PATH=MODEL_PATH):
#     """Make model prediction
#     Note: Model should exist in the given path

#     Parameters
#     ----------

#     param1 : str
#         MODEL_PATH: Path of the model

#     Returns
#     -----------
#     assertion
#         True if successful, False otherwise

#     Examples
#     ---------
#     >>> test_d_tree(MODEL_PATH=MODEL_PATH)
#     assert True

#     """

#     D_TREE = pickle.load(open(os.path.join(MODEL_PATH, "d_tree.pkl"), "rb"))
#     arr = np.asarray(
#         [
#             -1.21460000e02,
#             3.85200000e01,
#             2.90000000e01,
#             3.87300000e03,
#             7.97000000e02,
#             2.23700000e03,
#             7.06000000e02,
#             2.17360000e00,
#             5.48583569e00,
#             2.05783630e-01,
#             3.16855524e00,
#             1.00000000e00,
#             0.00000000e00,
#             0.00000000e00,
#             0.00000000e00,
#         ]
#     ).reshape(1, -1)

#     assert round(D_TREE.predict(arr)[0]) == 72100


# def test_rforest(MODEL_PATH=MODEL_PATH):
#     """Make model prediction
#     Note: Model should exist in the given path

#     Parameters
#     ----------

#     param1 : str
#         MODEL_PATH: Path of the model

#     Returns
#     -----------
#     assertion
#         True if successful, False otherwise

#     Examples
#     ---------
#     >>> test_rforest(MODEL_PATH=MODEL_PATH)
#     assert True

#     """

#     RFOREST_REG = pickle.load(open(os.path.join(MODEL_PATH, "random_forest.pkl"), "rb"))
#     arr = np.asarray(
#         [
#             -1.18390000e02,
#             3.41200000e01,
#             2.90000000e01,
#             6.44700000e03,
#             1.01200000e03,
#             2.18400000e03,
#             9.60000000e02,
#             8.28160000e00,
#             6.71562500e00,
#             1.56972235e-01,
#             2.27500000e00,
#             0.00000000e00,
#             0.00000000e00,
#             0.00000000e00,
#             0.00000000e00,
#         ]
#     ).reshape(1, -1)

#     assert round(RFOREST_REG.predict(arr)[0]) == 491164
