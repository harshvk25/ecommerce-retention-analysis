"""
E-commerce Customer Retention Analysis
Author: 24ds2000078@ds.study.iitm.ac.in
Date: December 2024
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Quarterly retention data
data = {
    'Quarter': ['Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024'],
    'Retention_Rate': [71.97, 72.36, 69.76, 72.37],
    'Industry_Target': [85, 85, 85, 85]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate statistics
average_retention = df['Retention_Rate'].mean()
gap_from_target = 85 - average_retention
percentage_gap = (gap_from_target / 85) * 100

print(f"Average Customer Retention Rate: {average_retention:.2f}")
print(f"Industry Target: 85")
print(f"Performance Gap: {gap_from_target:.2f} points")
print(f"Percentage Gap: {percentage_gap:.2f}%")

# Save to CSV
df.to_csv('retention_data.csv', index=False)
