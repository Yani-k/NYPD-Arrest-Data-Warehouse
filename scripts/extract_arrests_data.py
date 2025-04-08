import requests
import pandas as pd

# Socrata API endpoint for NYPD Arrests data
url = "https://data.cityofnewyork.us/resource/8h9b-rp9u.json"

# Fetch data from the API
response = requests.get(url)
data = response.json()

# Convert to DataFrame
arrests_df = pd.DataFrame(data)

# Save to CSV for further processing
arrests_df.to_csv("data/nypd_arrests.csv", index=False)
print("NYPD Arrests data extracted and saved.")
