import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../Dataset/cleaned_churn.csv")

# Churn Distribution
df["Churn"].value_counts().plot(kind="bar")
plt.title("Customer Churn Distribution")
plt.tight_layout()
plt.savefig("../Screenshots/churn_distribution.png")
plt.close()

# Contract Analysis
pd.crosstab(df["Contract"], df["Churn"]).plot(kind="bar")
plt.title("Contract Type vs Churn")
plt.tight_layout()
plt.savefig("../Screenshots/contract_analysis.png")
plt.close()

# Model Accuracy
plt.figure(figsize=(4,4))
plt.bar(["Random Forest"], [78.92])
plt.ylim(0,100)
plt.title("Model Accuracy")
plt.savefig("../Screenshots/model_accuracy.png")
plt.close()

print("Screenshots generated successfully!")