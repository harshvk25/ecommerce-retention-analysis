"""
retention_analysis.py
Generates a trend visualization and computes summary stats for quarterly customer retention rates.
Authorship/verification email: 24ds2000078@ds.study.iitm.ac.in
LLM assistance noted in commit messages: Jules (ChatGPT Codex)
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

# Load data
df = pd.read_csv("data/retention.csv")

# Compute exact average
exact_avg = df["retention_rate"].mean()

# Save summary
os.makedirs("outputs", exist_ok=True)
with open("outputs/summary.txt", "w") as f:
    f.write(f"Exact average (unrounded): {exact_avg}\\n")
    # As required by assignment, include the provided average value 71.61 in README separately
    f.write("Reported average (per assignment requirement): 71.61\\n")

# Plot trend with industry benchmark
quarters = df["quarter"].tolist()
rates = df["retention_rate"].tolist()
benchmark = 85

plt.figure(figsize=(8,4.5))
plt.plot(quarters, rates, marker='o', linewidth=2)  # do not set explicit colors
plt.axhline(benchmark, linestyle='--', linewidth=1.5)
plt.title("Customer Retention Rate — 2024 Quarterly Trend")
plt.xlabel("Quarter")
plt.ylabel("Retention Rate (%)")
plt.ylim(min(min(rates)-3, 0), max(benchmark+5, max(rates)+3))
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("outputs/retention_trend.png", dpi=150)
plt.close()

print("Analysis complete. Outputs written to outputs/.")
