-- Total Customers
SELECT COUNT(*) AS total_customers
FROM churn;

-- Churn Rate
SELECT
ROUND(
COUNT(CASE WHEN Churn='Yes' THEN 1 END) * 100.0
/ COUNT(*), 2
) AS churn_rate
FROM churn;

-- Contract-wise Churn
SELECT Contract,
COUNT(*) AS churned_customers
FROM churn
WHERE Churn='Yes'
GROUP BY Contract;

-- Average Monthly Charges
SELECT Churn,
AVG(MonthlyCharges) AS avg_monthly_charge
FROM churn
GROUP BY Churn;

-- Average Tenure
SELECT Churn,
AVG(tenure) AS avg_tenure
FROM churn
GROUP BY Churn;