-- Covid Dataset Analysis Queries
-- 1. Create table structure (if needed)
CREATE TABLE covid_data (
    Age INT,
    Gender VARCHAR(10),
    Fever DECIMAL(4, 1),
    Cough VARCHAR(10),
    City VARCHAR(50),
    Has_Covid VARCHAR(5)
);
-- 2. Basic Statistics
SELECT COUNT(*) as total_records,
    SUM(
        CASE
            WHEN Has_Covid = 'Yes' THEN 1
            ELSE 0
        END
    ) as positive_cases,
    SUM(
        CASE
            WHEN Has_Covid = 'No' THEN 1
            ELSE 0
        END
    ) as negative_cases,
    ROUND(
        SUM(
            CASE
                WHEN Has_Covid = 'Yes' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) as positivity_rate
FROM covid_data;
-- 3. Cases by City
SELECT City,
    COUNT(*) as total_people,
    SUM(
        CASE
            WHEN Has_Covid = 'Yes' THEN 1
            ELSE 0
        END
    ) as positive_cases,
    ROUND(
        SUM(
            CASE
                WHEN Has_Covid = 'Yes' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) as city_positivity_rate
FROM covid_data
GROUP BY City
ORDER BY positive_cases DESC;
-- 4. Gender Distribution of Covid Cases
SELECT Gender,
    COUNT(*) as total_count,
    SUM(
        CASE
            WHEN Has_Covid = 'Yes' THEN 1
            ELSE 0
        END
    ) as positive_cases
FROM covid_data
GROUP BY Gender;
-- 5. Average Fever by Covid Status
SELECT Has_Covid,
    AVG(Fever) as avg_fever,
    MIN(Fever) as min_fever,
    MAX(Fever) as max_fever
FROM covid_data
GROUP BY Has_Covid;
-- 6. Age Group Analysis
SELECT CASE
        WHEN Age < 18 THEN '0-17'
        WHEN Age BETWEEN 18 AND 35 THEN '18-35'
        WHEN Age BETWEEN 36 AND 60 THEN '36-60'
        ELSE '60+'
    END as age_group,
    COUNT(*) as total_count,
    SUM(
        CASE
            WHEN Has_Covid = 'Yes' THEN 1
            ELSE 0
        END
    ) as positive_cases
FROM covid_data
GROUP BY age_group
ORDER BY age_group;
-- 7. Cough Severity vs Covid
SELECT Cough,
    COUNT(*) as total_count,
    SUM(
        CASE
            WHEN Has_Covid = 'Yes' THEN 1
            ELSE 0
        END
    ) as positive_cases
FROM covid_data
GROUP BY Cough;