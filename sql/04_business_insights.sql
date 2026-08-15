-- ============================================================
-- Business Insights
-- ============================================================


-- 1. Access level vs reimbursement performance
-- Business question:
-- How does access level relate to reimbursement outcomes?

SELECT
    ma.access_level,
    ma.reimbursement_status,
    COUNT(*) AS record_count
FROM market_access ma
GROUP BY
    ma.access_level,
    ma.reimbursement_status
ORDER BY
    ma.access_level,
    record_count DESC;


-- 2. Average patient copay by region and access level
-- Business question:
-- How does patient copay vary across regions and
-- access levels?

SELECT
    r.region_name,
    ma.access_level,
    ROUND(AVG(ma.patient_copay), 2) AS avg_patient_copay
FROM market_access ma
JOIN regions r
    ON ma.region_id = r.region_id
GROUP BY
    r.region_name,
    ma.access_level
ORDER BY
    r.region_name,
    ma.access_level;


-- 3. Market volume by access level
-- Business question:
-- Which access level accounts for the highest
-- market volume?

SELECT
    access_level,
    SUM(volume) AS total_market_volume
FROM market_access
GROUP BY access_level
ORDER BY total_market_volume DESC;
