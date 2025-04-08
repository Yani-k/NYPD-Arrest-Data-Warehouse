-- Staging table for NYPD Arrests data
WITH arrests_cleaned AS (
    SELECT 
        arrest_key,
        arrest_date,
        precinct,
        jurisdiction_code,
        age_group,
        perp_sex,
        perp_race,
        law_code,
        law_cat_cd,
        latitude,
        longitude
    FROM `project_id.dataset_id.nypd_arrests`
    WHERE arrest_date BETWEEN '2010-01-01' AND '2024-12-31'
)
SELECT * FROM arrests_cleaned;
