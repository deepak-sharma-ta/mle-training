import pickle
import sys
import os
import pandas as pd
import numpy as np

sys.path.append("/home/deepak/practice_git_repo/assignment2/mle-training/")

from src.ingest_data import (
    load_housing_data,
)

MODEL_PATH = "/home/deepak/practice_git_repo/assignment2/mle-training/artifacts/"
PATH = "data/raw/"


def test_loaded_df_type(path=PATH):
    """Loads to the dataframe and makes assertion

    :param path: Path of the csv file
    :returns: An assertion

    >>> test_loaded_df_type('src/app.py')
    assert True
    """
    path = os.path.join(os.getcwd(), path)
    df = load_housing_data(housing_path=path)  # requires csv file in the correct path
    assert isinstance(df, pd.DataFrame)


def test_lin_reg(MODEL_PATH=MODEL_PATH):
    """Make model prediction

    Note: Model should exist in the given path

    :param MODEL_PATH: Path of the model
    :returns: An assertion

    >>> test_lin_reg(MODEL_PATH=MODEL_PATH)
    assert True
    """
    LIN_REG = pickle.load(open(os.path.join(MODEL_PATH, "lin_reg.pkl"), "rb"))
    arr = np.asarray(
        [
            -1.21460000e02,
            3.85200000e01,
            2.90000000e01,
            3.87300000e03,
            7.97000000e02,
            2.23700000e03,
            7.06000000e02,
            2.17360000e00,
            5.48583569e00,
            2.05783630e-01,
            3.16855524e00,
            1.00000000e00,
            0.00000000e00,
            0.00000000e00,
            0.00000000e00,
        ]
    ).reshape(1, -1)

    assert round(LIN_REG.predict(arr)[0]) == 85658


def test_d_tree(MODEL_PATH=MODEL_PATH):
    """Make model prediction

    Note: Model should exist in the given path

    :param MODEL_PATH: Path of the model
    :returns: An assertion

    >>> test_d_tree(MODEL_PATH=MODEL_PATH)
    assert True
    """
    D_TREE = pickle.load(open(os.path.join(MODEL_PATH, "d_tree.pkl"), "rb"))
    arr = np.asarray(
        [
            -1.21460000e02,
            3.85200000e01,
            2.90000000e01,
            3.87300000e03,
            7.97000000e02,
            2.23700000e03,
            7.06000000e02,
            2.17360000e00,
            5.48583569e00,
            2.05783630e-01,
            3.16855524e00,
            1.00000000e00,
            0.00000000e00,
            0.00000000e00,
            0.00000000e00,
        ]
    ).reshape(1, -1)

    assert round(D_TREE.predict(arr)[0]) == 72100


def test_rforest(MODEL_PATH=MODEL_PATH):
    """Make model prediction

    Note: Model should exist in the given path

    :param MODEL_PATH: Path of the model
    :returns: An assertion

    >>> test_rforest(MODEL_PATH=MODEL_PATH)
    assert True
    """
    RFOREST_REG = pickle.load(open(os.path.join(MODEL_PATH, "random_forest.pkl"), "rb"))
    arr = np.asarray(
        [
            -1.18390000e02,
            3.41200000e01,
            2.90000000e01,
            6.44700000e03,
            1.01200000e03,
            2.18400000e03,
            9.60000000e02,
            8.28160000e00,
            6.71562500e00,
            1.56972235e-01,
            2.27500000e00,
            0.00000000e00,
            0.00000000e00,
            0.00000000e00,
            0.00000000e00,
        ]
    ).reshape(1, -1)

    assert round(RFOREST_REG.predict(arr)[0]) == 491164
