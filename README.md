# NYPD Arrests and NYC 311 Complaints Analysis

## Project Description
This project explores the relationship between public safety-related complaints reported to NYC's 311 service and the types of arrests made by the NYPD across various neighborhoods in New York City. By integrating NYC 311 Service Requests data with NYPD Arrests data, the project identifies patterns that demonstrate how community-reported issues may correlate with law enforcement actions. The analysis spans arrest data from 2006 to the most recent year and complaint data from 2010 onward.

## Key objectives include:

Investigating whether neighborhoods with higher complaint volumes experience more arrests.

Identifying the types of complaints most predictive of arrests.

Analyzing trends in arrests by demographics, offense types, and geographic locations.

## Technologies and Tools Used

Python: Data extraction and profiling.

Google BigQuery: Data storage and querying.

DBT (Data Build Tool): Data transformation and modeling.

LucidChart: Dimensional model design.

Tableau: Data visualization and dashboard creation.

Google Storage: Intermediate data storage.

YData Profiling: Data profiling for quality checks.

## Data Sources

NYPD Arrests Data

Source: NYC Open Data

URL: Public dataset on crime type, location, and enforcement timing (2006–present).

NYC 311 Service Requests Data

Source: NYC Open Data

URL: Public dataset on complaints related to safety, infrastructure, and quality of life (2010–present).

## Project Workflow

ETL Process:

Extracted NYPD Arrests data using Python and Socrata API.

Loaded data into Google BigQuery after profiling and cleaning.

Used public BigQuery datasets for NYC 311 complaints due to extraction challenges.

Data Modeling:

Created staging tables for both datasets.

Designed dimensional models with surrogate keys for attributes like location, demographics, and offense type.

Built fact tables by joining source tables with dimension tables.

## Analysis & Visualization:

Conducted trend analysis on arrests and complaints by borough, gender, age group, and offense type.

Developed interactive Tableau dashboards for insights.

## Key Insights

Brooklyn leads in both arrests and complaints, highlighting urban management challenges.

Males aged 25–44 account for the majority of arrests, particularly for offenses like assault.

Noise complaints (residential) are the most frequent, followed by heat/hot water issues and illegal parking.

Complaints peaked between 2018–2020, indicating persistent quality-of-life concerns.

## Proposed Benefits

Enhanced decision-making through consolidated data analysis.

Scalable system capable of handling growing datasets.

Faster query performance with optimized schemas.

Improved data quality via standardized ETL processes.

User-friendly insights through interactive dashboards.

## Challenges Faced

Handling large datasets during extraction and profiling.

Learning new tools like DBT for transformations and Tableau for visualizations.

Managing discrepancies in location data between datasets.

## Future Recommendations
Centralize all datasets in a unified repository for easier access and integration.

Develop real-time dashboards to monitor emerging trends dynamically.

Incorporate predictive analytics to forecast future trends based on historical data.

## Contributors
Khan Yunus, Abdullah Alam, Sahla Mokaria, Jyoti Nagar, Jesse Sit

