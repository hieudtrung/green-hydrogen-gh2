# Green Hydrogen

## Introduction

Also known as **GH2**, this repository hosts the software part of my semester project at SDU Mechatronics, Fall 2023. The motivation behind it can be found [here](https://www.notion.so/hdtcollab/Green-Hydrogen-bb72d77625bd4cf4a076ea8007fbf551?pvs=4
). In short, it is an AI-powered management system for green hydrogen production that uses only electricity from wind farms and national grid.

The software architecture design is descsribed [here](#architecture-design), while mechanical, electrical & electronics design, and test bench results are not yet disclosed.

## Getting Started

### Development Environment Setup

1. Clone the source code

    ```bash
    git clone https://dagshub.com/hieudtrung/mlo.git \
    cd mlo
    ```

2. Create a virtual environment
    by using either `conda` or `mamba`

    ```bash
    conda install -f conda_env.yaml
    ```

3. *(optional)* Setup DagsHub for experiment tracking & data versioning

    ```bash
    # MLFlow with DagsHub Experiment as host
    export MLFLOW_TRACKING_URI=https://dagshub.com/hieudtrung/green-hydrogen-gh2.mlflow \
    export MLFLOW_TRACKING_USERNAME=<your_username> \
    export MLFLOW_TRACKING_PASSWORD=<your_password>

    # DVC with DagsHub as remote storage
    dvc remote add origin https://dagshub.com/hieudtrung/green-hydrogen-gh2.dvc
    dvc remote modify origin --local auth basic 
    dvc remote modify origin --local user hieudtrung 
    dvc remote modify origin --local password <your_token>

    # DVC with MinIO as remote storage
    dvc remote add origin s3://dvc
    dvc remote modify origin endpointurl s3://gh2-emu-trials
    dvc remote modify origin --local access_key_id <your_token> \
    dvc remote modify origin --local password secret_access_key <your_token>
    ```

4. *(optional)* CICD with Github Actions

    Retraining our model with newer data is a tedious task which can be automated. First, we follow [this guide](https://dagshub.com/docs/integration_guide/github/index.html) to sync DagsHub repo with Github.

    Then, create a Github Actions config so that any code update triggers CI pipelines to run.

### Reproduce the results

A Docker-compose file is also available for you to self-host on your own PC. Note that it is not fully tested.

## Architecture Design

### Sequence Diagrams

### Overall Architecture

This picture reveals the overall system. For more details about each service's structure & communication protocol, please  find them in their corresponding README document.

## Contribute

This work is published under MIT license as a showcase of my skills. If you have any issue or update requirement, please log an issue. Feel free to fork, redistribute, or use as your own good.
