/* Owner: Sharol George (M2) | Model: stg_ehr_events.sql */

WITH source_data AS (
    SELECT * 
    FROM {{ source('raw_ehr', 'raw_events') }}
),

cleaned_data AS (
    SELECT DISTINCT
        CAST(case_id AS STRING) AS case_id,
        TRIM(LOWER(activity_name)) AS activity_name,
        CAST(event_timestamp AS TIMESTAMP) AS timestamp,
        TRIM(resource) AS resource,
        TRIM(department) AS department,
        TRIM(patient_age_group) AS age_group
    FROM source_data
    WHERE case_id IS NOT NULL 
      AND event_timestamp IS NOT NULL
)

SELECT * FROM cleaned_data
