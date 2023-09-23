# Green Hydrogren

## Introduction

Also known as **GH2**, this repository hosts the software part of my thesis at SDU Mechatronics 2023. The motivation behind it can be found [here](https://www.notion.so/hdtcollab/Green-Hydrogen-bb72d77625bd4cf4a076ea8007fbf551?pvs=4
). In other words, it's a showdown between reinforcement learning and optimal control in the context of energy distribution.

Other parts including mechanical design, electrical & electronics design, report and publication are disclosed [here]().

## Getting Started

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

3. Setup DagsHub for experiment tracking & data versioning

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

    First, we follow [this guide](https://dagshub.com/docs/integration_guide/github/index.html) to sync DagsHub repo with Github.

    Then, create a Github Actions config so that any code update triggers CI pipelines to run.

## Usage

### Reproduce the results

### Train from your own data

### Serve as REST API

## Contribute
