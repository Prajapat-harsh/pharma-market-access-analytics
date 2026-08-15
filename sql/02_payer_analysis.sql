-- ============================================================
-- Payer Analysis
-- ============================================================


-- 1. Reimbursement rate by payer
-- Business question:
-- Which payers have the highest reimbursement rates?

SELECT
    p.payer_name,
    ROUND(
        100.0 * COUNT(*) FILTER (
            WHERE ma.reimbursement_status = 'Reimbursed'
        ) / COUNT(*),
        2
    ) AS reimbursement_rate
FROM payers p
JOIN payer_product_access ppa
    ON p.payer_id = ppa.payer_id
JOIN market_access ma
    ON ppa.ppa_id = ma.ppa_id
GROUP BY p.payer_name
ORDER BY reimbursement_rate DESC;


-- 2. Product access status by payer
-- Business question:
-- How are product access statuses distributed across payers?

SELECT
    p.payer_name,
    ppa.access_status,
    COUNT(*) AS product_count
FROM payers p
JOIN payer_product_access ppa
    ON p.payer_id = ppa.payer_id
GROUP BY
    p.payer_name,
    ppa.access_status
ORDER BY
    p.payer_name,
    product_count DESC;


-- 3. Average patient copay by payer
-- Business question:
-- Which payers have the highest average patient copay?

SELECT
    p.payer_name,
    ROUND(AVG(ma.patient_copay), 2) AS avg_patient_copay
FROM payers p
JOIN payer_product_access ppa
    ON p.payer_id = ppa.payer_id
JOIN market_access ma
    ON ppa.ppa_id = ma.ppa_id
GROUP BY p.payer_name
ORDER BY avg_patient_copay DESC;
