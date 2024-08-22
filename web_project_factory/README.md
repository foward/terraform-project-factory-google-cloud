# Web UI to create projects on Demand using the terraform module of Project Factory

## Project Description
This project aims to simplify the process of creating projects on Google Cloud using the Terraform module of Project Factory. It leverages GitLab for version control and implements GitOps principles for project creation.

To get started, you will need a GitLab token and the folder number where the project YAML file is committed. This information is required to initiate the GitOps process, where the project creation request can be reviewed and approved by the admin.

By following the installation and usage instructions provided below, you will be able to easily create projects on Google Cloud using the Terraform module and GitLab integration.

## Installation

### Prerequisites
- Python 3.x
- pip

### Setting Up a Virtual Environment
...
### Alternative Setup
...
## Usage
...

## Installation

### Prerequisites
- Python 3.x
- pip

### Setting Up a Virtual Environment

1. **Install virtualenv**:
    ```bash
    pip3 install virtualenv
    ```

2. **Create a virtual environment**:
    ```bash
    virtualenv venv
    ```

3. **Activate the virtual environment**:
    ```bash
    source venv/bin/activate
    ```

4. **Deactivate the virtual environment**:
    ```bash
    deactivate
    ```

### Alternative Setup

1. **Navigate to your project directory**:
    ```bash
    cd your-project
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv env
    ```

3. **Activate the virtual environment**:
    ```bash
    source env/bin/activate
    ```

4. **Install dependencies**:
    ```bash
    pip3 install -r requirements.txt
    ```

## Usage

To run the main script, use the following command:
```bash
python main.py