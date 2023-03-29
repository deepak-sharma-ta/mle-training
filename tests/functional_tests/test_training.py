import os
import pickle
import argparse
import numpy as np
import pandas as pd
from scipy.stats import randint
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.tree import DecisionTreeRegressor


PATH = "/home/deepak/practice_git_repo/assignment2/mle-training/data/processed"
housing_prepared = pd.read_csv(os.path.join(PATH, "housing_prepared.csv"))
housing_labels = pd.read_csv(os.path.join(PATH, "housing_labels.csv"))
column_names = [
    "longitude",
    "latitude",
    "housing_median_age",
    "total_rooms",
    "total_bedrooms",
    "population",
    "households",
    "median_income",
    "rooms_per_household",
    "bedrooms_per_room",
    "population_per_household",
    "ocean_proximity_INLAND",
    "ocean_proximity_ISLAND",
    "ocean_proximity_NEAR BAY",
    "ocean_proximity_NEAR OCEAN",
]


def test_lin_reg_train(
    housing_prepared=housing_prepared, housing_labels=housing_labels
):
    assert len(housing_labels) == len(housing_prepared)
    assert isinstance(housing_prepared.values, np.ndarray)
    assert isinstance(housing_labels.values, np.ndarray)

    assert sorted(housing_prepared.columns.to_list()) == sorted(column_names)
