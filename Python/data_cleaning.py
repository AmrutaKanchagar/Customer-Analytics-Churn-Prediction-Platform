import pandas as pd

# Try reading as comma-separated
try:
    df = pd.read_csv("../Dataset/Telco-Customer-Churn.csv")
    
    # If only one column exists, file is probably tab-separated
    if len(df.columns) == 1:
        df = pd.read_csv(
            "../Dataset/Telco-Customer-Churn.csv",
            sep="\t"
        )

except Exception as e:
    print("Error reading file:", e)
    exit()

print("Columns:")
print(df.columns)

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert TotalCharges to numeric if present
if "TotalCharges" in df.columns:
    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"],
        errors="coerce"
    )

    df["TotalCharges"] = df["TotalCharges"].fillna(
        df["TotalCharges"].median()
    )

# Save cleaned data
df.to_csv(
    "../Dataset/cleaned_churn.csv",
    index=False
)

print("\nData cleaned successfully!")
print("Cleaned file saved as cleaned_churn.csv")