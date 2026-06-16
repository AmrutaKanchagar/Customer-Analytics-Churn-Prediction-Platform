# Customer Analytics & Churn Prediction Platform

## Overview

Customer churn is one of the most critical challenges faced by subscription-based businesses. This project focuses on analyzing customer behavior, identifying factors contributing to customer attrition, and building a machine learning solution to predict customer churn.

The project combines Data Analytics, Machine Learning, SQL, and Business Intelligence concepts to provide actionable insights that help organizations improve customer retention and reduce revenue loss.

---

## Business Problem

Customer retention is significantly more cost-effective than customer acquisition. Organizations need to understand:

- Why customers leave
- Which customer segments are at high risk
- What factors influence churn behavior
- How retention strategies can be improved

This project addresses these challenges through data-driven analysis and predictive modeling.

---

## Objectives

- Analyze customer behavior and churn trends
- Identify key factors affecting customer retention
- Perform data cleaning and preprocessing
- Build a machine learning model for churn prediction
- Generate actionable business insights
- Support data-driven decision making

---

## Dataset

**Dataset Used:** IBM Telco Customer Churn Dataset

The dataset contains customer information including:

- Customer ID
- Gender
- Senior Citizen Status
- Partner Status
- Dependents
- Tenure
- Internet Service
- Contract Type
- Payment Method
- Monthly Charges
- Total Charges
- Churn Status

### Dataset Statistics

| Metric | Value |
|----------|----------|
| Total Records | 7043 |
| Features | 21 |
| Churned Customers | 1869 |
| Retained Customers | 5174 |

---

## Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Data Analysis & Machine Learning |
| Pandas | Data Cleaning & Transformation |
| NumPy | Numerical Operations |
| Scikit-Learn | Churn Prediction Model |
| SQL | Business Queries & Analysis |
| Git & GitHub | Version Control |
| Power BI | Business Intelligence Dashboard *(Planned)* |

---

## Project Structure

```text
Customer-Analytics-Churn-Prediction/

│
├── Dataset/
│   ├── Telco-Customer-Churn.csv
│   └── cleaned_churn.csv
│
├── Python/
│   ├── data_cleaning.py
│   ├── analysis.py
│   └── churn_prediction.py
│
├── SQL/
│   └── churn_queries.sql
│
├── PowerBI/
│
├── Screenshots/
│
├── requirements.txt
│
└── README.md
```

---

## Workflow

### 1. Data Cleaning

Performed:

- Data loading
- Duplicate removal
- Data validation
- Missing value inspection
- Data type conversion

Output:

```text
cleaned_churn.csv
```

---

### 2. Exploratory Data Analysis

Analyzed:

- Customer churn distribution
- Contract type impact
- Monthly charges
- Customer tenure
- Customer retention trends

---

### 3. Machine Learning

Algorithm Used:

- Random Forest Classifier

Steps:

- Feature Engineering
- Data Encoding
- Train-Test Split
- Model Training
- Model Evaluation

---

## Model Performance

### Churn Prediction Accuracy

```text
78.92%
```

The model successfully predicts customer churn behavior using customer demographic and service-related attributes.

---

## Key Findings

### 1. Churn Rate

- Total Customers: 7043
- Churned Customers: 1869
- Churn Rate: 26.54%

### 2. Contract Type Analysis

| Contract Type | Churned Customers |
|---------------|-------------------|
| Month-to-Month | 1655 |
| One Year | 166 |
| Two Year | 48 |

**Insight:**
Month-to-month customers are significantly more likely to churn.

---

### 3. Monthly Charges

| Customer Type | Average Monthly Charges |
|--------------|-------------------------|
| Retained Customers | 61.27 |
| Churned Customers | 74.44 |

**Insight:**
Customers with higher monthly charges tend to churn more frequently.

---

### 4. Customer Tenure

| Customer Type | Average Tenure |
|--------------|---------------|
| Retained Customers | 37.57 Months |
| Churned Customers | 17.98 Months |

**Insight:**
Customers with shorter tenure are more likely to leave the company.

---

## Business Recommendations

Based on the analysis:

### Recommendation 1

Promote long-term contracts through discounts and loyalty programs.

### Recommendation 2

Improve onboarding experience for new customers.

### Recommendation 3

Provide personalized offers for customers with high monthly charges.

### Recommendation 4

Improve customer support and engagement strategies.

---

## SQL Analytics

The project includes SQL queries for:

- Total Customer Analysis
- Churn Rate Calculation
- Contract-wise Churn Analysis
- Revenue Insights
- Customer Segmentation

---

## Future Enhancements

- Power BI Interactive Dashboard
- Streamlit Web Application
- Advanced Machine Learning Models
- Customer Lifetime Value Prediction
- Real-Time Churn Prediction System
- Cloud Deployment (AWS/GCP)

---

## Business Impact

This project demonstrates how data analytics and machine learning can help organizations:

- Reduce customer attrition
- Improve customer retention
- Increase revenue
- Support strategic decision-making
- Identify high-risk customers proactively

---

## Author

**Amruta Kanchagar**

Aspiring Data Analyst | Python | SQL | Power BI | Machine Learning

---

## License

This project is developed for educational and portfolio purposes.