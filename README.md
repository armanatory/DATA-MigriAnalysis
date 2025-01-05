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

### consumer_price_index.csv

The Consumer Price Index (CPI) data is retrieved using the script located at `scripts/consumer_price_index_query.py`. This script sends a POST request to the Statistics Finland API to fetch monthly CPI data starting from 2015. The data is saved in a CSV file at `data/consumer_price_index.csv` with the following structure:

- **Date**: The year and month in the format `YYYY-MM` (e.g., `2018-11`).
- **CPI**: The consumer price index value for that month.

This data enables the analysis of inflation trends and price level changes over time.

## Notebooks

### Migri_Salary_Comparison_2018_2025.ipynb
This notebook performs a comparative analysis of the minimum salary requirements for different residence permit types in Finland from 2018 to 2025. It utilizes the data from `migri_residence_premit_salary_requirements_2018_2025.csv` and `consumer_price_index.csv` to visualize trends and draw insights. The analysis includes:

- Loading and preprocessing the data.
- Adjusting salary requirements for inflation using the Consumer Price Index (CPI).
- Visualizing the trends in salary requirements over the years.
- Comparing the salary requirements across different permit types.

The results provide a clear understanding of how the minimum salary requirements have evolved and how they compare to inflation trends.

## Scripts

### consumer_price_index_query.py

The `consumer_price_index_query.py` script is responsible for fetching the Consumer Price Index (CPI) data from the Statistics Finland API. It sends a POST request to the API to retrieve monthly CPI data starting from 2015. The script processes the received data and saves it in a CSV file located at `data/consumer_price_index.csv`. This data is crucial for adjusting salary requirements for inflation and analyzing price level changes over time.


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