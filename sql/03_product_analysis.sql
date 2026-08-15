-- ============================================================
-- Product Analysis
-- ============================================================


-- 1. Total market volume by product
-- Business question:
-- Which products have the highest market volume?

SELECT
    p.product_name,
    SUM(ma.volume) AS total_market_volume
FROM products p
JOIN payer_product_access ppa
    ON p.product_id = ppa.product_id
JOIN market_access ma
    ON ppa.ppa_id = ma.ppa_id
GROUP BY p.product_name
ORDER BY total_market_volume DESC;


-- 2. Product ranking by market volume
-- Business question:
-- How do products rank based on their total market volume?

SELECT
    p.product_name,
    SUM(ma.volume) AS total_market_volume,
    RANK() OVER (
        ORDER BY SUM(ma.volume) DESC
    ) AS volume_rank
FROM products p
JOIN payer_product_access ppa
    ON p.product_id = ppa.product_id
JOIN market_access ma
    ON ppa.ppa_id = ma.ppa_id
GROUP BY p.product_name
ORDER BY volume_rank;
