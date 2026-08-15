-- ============================================================
-- Market Access Analysis
-- ============================================================


-- 1. Average patient copay by access level
-- Business question:
-- How does average patient copay vary by access level?

SELECT
    access_level,
    ROUND(AVG(patient_copay), 2) AS avg_patient_copay
FROM market_access
GROUP BY access_level
ORDER BY avg_patient_copay DESC;


-- 2. Restriction distribution by access level
-- Business question:
-- What types of restrictions are most common at each access level?

SELECT
    access_level,
    restrictions,
    COUNT(*) AS record_count,
    SUM(COUNT(*)) OVER (
        PARTITION BY access_level
    ) AS access_level_total,
    ROUND(
        100.0 * COUNT(*) /
        SUM(COUNT(*)) OVER (
            PARTITION BY access_level
        ),
        2
    ) AS restriction_percentage
FROM market_access
GROUP BY access_level, restrictions
ORDER BY access_level, record_count DESC;


-- 3. Access-level distribution
-- Business question:
-- What proportion of market-access records fall
-- into each access level?

SELECT
    access_level,
    COUNT(*) AS record_count,
    ROUND(
        100.0 * COUNT(*) /
        SUM(COUNT(*)) OVER (),
        2
    ) AS percentage_of_records
FROM market_access
GROUP BY access_level
ORDER BY record_count DESC;
