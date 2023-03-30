from setuptools import setup

setup(
    name="housing_package",
    version="0.0.1",
    install_requires=[
        "requests",
        'importlib-metadata; python_version == "3.10.9"',
        "argparse",
        "numpy",
        "pandas",
        "scikit-learn",
    ],
)
