import requests
import pandas as pd

# API Endpoint
API_URL = "https://pxdata.stat.fi:443/PxWeb/api/v1/en/StatFin/khi/statfin_khi_pxt_11xb.px"

# JSON Payload
payload = {
    "query": [
        {
            "code": "Hyödyke",
            "selection": {
                "filter": "item",
                "values": ["0"]
            }
        },
        {
            "code": "Tiedot",
            "selection": {
                "filter": "item",
                "values": ["indeksipisteluku"]
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
    values = data["value"]

    # Create a DataFrame
    df = pd.DataFrame({
        "Date": months.values(),
        "CPI": values
    })

    # Convert Date column to a readable format (e.g., "2018M11" to "2018-11")
    df["Date"] = df["Date"].str.replace("M", "-")

    # Save the DataFrame to CSV
    output_filename = "data/consumer_price_index.csv"
    df.to_csv(output_filename, index=False)

    print(f"Data saved successfully to {output_filename}")
else:
    print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
