# Median housing value prediction

The housing data can be downloaded from https://raw.githubusercontent.com/ageron/handson-ml/master/. The script has codes to download the data. We have modelled the median house value on given housing data. 

The following techniques have been used: 

 - Linear regression
 - Decision Tree
 - Random Forest

## Steps performed
 - We prepare and clean the data. We check and impute for missing values.
 - Features are generated and the variables are checked for correlation.
 - Multiple sampling techniques are evaluated. The data set is split into train and test.
 - All the above said modelling techniques are tried and evaluated. The final metric used to evaluate is (root) mean squared error, MAE.

#### To pull the docker image from docker hub:
    -> Link to docker image: https://hub.docker.com/r/deepaksharma1997/housing_docker

    -> docker pull deepaksharma1997/housing_docker:latest

    -> docker run -dit --name housing_docker deepaksharma1997/housing_docker:latest

    ## Go inside the conatiner as root user:
    -> docker exec -u 0 -it housing_docker bash

    ## To create and activate the environment
    -> conda env create -f app/deploy/conda/linux_cpu_py310.yml <br>

    -> conda activate mle-dev-docker<br>

    # To download the CSV file<br>
    -> cd app/

    -> python3 src/housing_package/ingest_data.py<br>

    # To display the supported command line arguments<br>
    -> python3 src/housing_package/ingest_data.py -h<br> 

    # To Train with the dataset<br>
    -> python3 src/housing_package/train.py<br>

    # To display the supported command line arguments<br>
    -> python3 src/housing_package/train.py -h<br> 

    # To evaluate the trained model<br>
    -> python3 src/housing_package/score.py<br>

    # To display the supported command line arguments<br>
    -> python3 src/housing_package/score.py -h<br>

#### To create the docker image:
    -> docker build -t housing_docker .

    ## To run the container
    docker run -dit --name housing_docker housing_docker

    ## Go inside the conatiner as root user:
    -> docker exec -u 0 -it housing_docker bash

    ## To create and activate the environment
    -> conda env create -f app/deploy/conda/linux_cpu_py310.yml <br>

    -> conda activate mle-dev-docker<br>

    # To download the CSV file<br>
    -> cd app/

    -> python3 src/housing_package/ingest_data.py<br>

    # To display the supported command line arguments<br>
    -> python3 src/housing_package/ingest_data.py -h<br> 

    # To Train with the dataset<br>
    -> python3 src/housing_package/train.py<br>

    # To display the supported command line arguments<br>
    -> python3 src/housing_package/train.py -h<br> 

    # To evaluate the trained model<br>
    -> python3 src/housing_package/score.py<br>

    # To display the supported command line arguments<br>
    -> python3 src/housing_package/score.py -h<br>