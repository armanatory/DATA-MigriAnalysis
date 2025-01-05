# DATA-MigriAnalysis
An analysis of data from the Finnish Immigration Service (Migri)

## Overview

## Data

### migri_residence_premit_salary_requirements_2018_2025.csv

The data is collected via sampling from archive.org. For each year, the latest available date is considered the value for that year. The data is stored in a CSV file with the following structure:

- **archive_date**: The date the data was archived.
- **year**: The year to which the data corresponds.
- **amount**: The minimum salary requirement for each type in euro.
- **type**: The permit type (e.g., erityisasiantuntija, eu-n-sininenkortti, tyontekijan-oleskelulupa; meaning specialist, EU Blue Card, and residence permit for an employee, respectively).

- **archive_url**: The source URL from archive.org.

The CSV file serves as the foundation for analyzing trends in salary requirements over the years.

## Notebooks

## How to Use

1. Clone the repository.
2. Using conda (https://www.anaconda.com/download) to create a new environment and install the required packages.
    Environment: datafinnishholidays

    ```bash
    conda create --name datamigri
    conda activate datamigri
    ```

3. Install the required Python packages:
   ```bash
    python -m pip install pandas numpy matplotlib seaborn requests
    ```
4. Run the analysis script in Jupyter Notebook to generate the results. I personally use [Jupyter notebook extension in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)