import requests
import pandas as pd

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
    
    # Extracting dimensions and values
    months = data["dimension"]["Kuukausi"]["category"]["label"]
    industries = data["dimension"]["Toimiala"]["category"]["label"]
    values = data["value"]

    # Reshape the values into a DataFrame
    df = pd.DataFrame(values, columns=["Index Value"])
    
    # Expand months and industries into readable format
    df["Date"] = list(months.values()) * len(industries)
    df["Industry"] = sum([[industry] * len(months) for industry in industries.values()], [])
    
    # Convert Date column to a readable format (e.g., "1995M01" to "1995-01")
    df["Date"] = df["Date"].str.replace("M", "-", regex=False)

    # Pivot table for better readability
    df_pivot = df.pivot(index="Date", columns="Industry", values="Index Value")
    df_pivot.reset_index(inplace=True)

    # Save the DataFrame to CSV
    output_filename = "data/wage_and_salary_indices.csv"
    df_pivot.to_csv(output_filename, index=False)

    print(f"Data saved successfully to {output_filename}")
else:
    print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
