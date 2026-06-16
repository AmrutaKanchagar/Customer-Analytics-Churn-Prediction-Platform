import pandas as pd

df = pd.read_csv("../Dataset/cleaned_churn.csv")

print("\n========== CUSTOMER CHURN ANALYSIS ==========\n")

print("Total Customers:", len(df))

print("\nChurn Distribution:")
print(df["Churn"].value_counts())

print("\nChurn Percentage:")
print((df["Churn"].value_counts(normalize=True) * 100).round(2))

print("\nContract Type vs Churn:")
print(pd.crosstab(df["Contract"], df["Churn"]))

print("\nAverage Monthly Charges:")
print(df.groupby("Churn")["MonthlyCharges"].mean().round(2))

print("\nAverage Tenure:")
print(df.groupby("Churn")["tenure"].mean().round(2))