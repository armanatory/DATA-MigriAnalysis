import requests
import pandas as pd
import numpy as np

# API Endpoint
API_URL = "https://pxdata.stat.fi:443/PxWeb/api/v1/en/StatFin/ktps/statfin_ktps_pxt_14mr.px"

# JSON Payload
payload = {
    "query": [
        {
            "code": "Toimiala",
            "selection": {
                "filter": "item",
                "values": [
                    "ATX",       # Whole economy
                    "ATXS11",    # Private sector
                    "O_P_Q"      # Public sector
                ]
            }
        },
        {
            "code": "Tiedot",
            "selection": {
                "filter": "item",
                "values": [
                    "alkuperainen"  # Original index series
                ]
            }
        }
    ],
    "response": {
        "format": "json-stat2"
    }
}

# Send POST request
response = requests.post(API_URL, json=payload)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    
    # Extract dimensions and values
    months = list(data["dimension"]["Kuukausi"]["category"]["label"].values())
    industries = list(data["dimension"]["Toimiala"]["category"]["label"].values())
    values = data["value"]

    # Reshape the values into rows corresponding to months and industries
    rows_per_month = len(industries)  # Number of industries per row
    reshaped_values = np.array(values).reshape(-1, rows_per_month)

    # Create a DataFrame
    df = pd.DataFrame(reshaped_values, columns=industries)
    df.insert(0, "Date", months)  # Insert the Date column at the beginning

    # Replace "null" with NaN for proper handling of missing values
    df.replace("null", np.nan, inplace=True)

    # Convert Date column to a readable format (e.g., "1995M01" to "1995-01")
    df["Date"] = df["Date"].str.replace("M", "-", regex=False)

    # Save the DataFrame to a CSV file
    output_filename = "data/wage_and_salary_indices.csv"
    df.to_csv(output_filename, index=False)

    print(f"Data saved successfully to {output_filename}")
else:
    print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
