from google.cloud import bigquery

# Initialize BigQuery client
client = bigquery.Client()

# Query for 311 complaints data in BigQuery public dataset
query = """
SELECT *
FROM `bigquery-public-data.new_york_311.311_service_requests`
WHERE created_date >= '2010-01-01'
"""
complaints_df = client.query(query).to_dataframe()

# Save to CSV
complaints_df.to_csv("data/nyc_311_complaints.csv", index=False)
print("NYC 311 Complaints data extracted and saved.")
