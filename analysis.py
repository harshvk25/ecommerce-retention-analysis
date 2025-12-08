import pandas as pd
import matplotlib.pyplot as plt

# Quarterly Retention Data
quarters = ["Q1", "Q2", "Q3", "Q4"]
retention_rates = [67.7, 72.8, 76.09, 74.75]

# Create DataFrame
df = pd.DataFrame({
    "Quarter": quarters,
    "Customer Retention Rate": retention_rates
})

# Calculate average retention
average_retention = round(df["Customer Retention Rate"].mean(), 2)
industry_target = 85

print("Average Retention Rate:", average_retention)

# Plot trend and benchmark
plt.figure(figsize=(8, 5))
plt.plot(df["Quarter"], df["Customer Retention Rate"], marker="o", label="Actual Retention")
plt.axhline(y=industry_target, linestyle="--", label="Industry Target (85)")
plt.axhline(y=average_retention, linestyle=":", label=f"Average (72.84)")

plt.title("Customer Retention Trend - 2024")
plt.xlabel("Quarter")
plt.ylabel("Retention Rate")
plt.legend()
plt.grid(True)

# Save visualization
plt.savefig("retention_trend.png", dpi=128)
plt.close()

print("Visualization saved as retention_trend.png")
