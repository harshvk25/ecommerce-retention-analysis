"""
Retention Rate Visualization
Generated with LLM assistance (ChatGPT Codex)
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('retention_data.csv')

# Create visualization
plt.figure(figsize=(12, 6))

# Plot retention rate
plt.plot(df['Quarter'], df['Retention_Rate'], 
         marker='o', linewidth=3, markersize=10, 
         label='Actual Retention', color='#2E86AB')

# Plot industry target
plt.axhline(y=85, color='#A23B72', linestyle='--', 
            linewidth=3, label='Industry Target (85)')

# Calculate and plot average
average_rate = df['Retention_Rate'].mean()
plt.axhline(y=average_rate, color='#F18F01', 
            linestyle=':', linewidth=2, 
            label=f'Average ({average_rate:.2f})')

# Fill performance gap
plt.fill_between(df['Quarter'], df['Retention_Rate'], 85, 
                  where=(df['Retention_Rate'] < 85), 
                  color='#C73E1D', alpha=0.3, 
                  label='Performance Gap')

# Customize plot
plt.title('E-commerce Customer Retention Rate Analysis 2024', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Quarter', fontsize=12)
plt.ylabel('Retention Rate (%)', fontsize=12)
plt.legend(loc='lower right')
plt.grid(True, alpha=0.3)
plt.ylim(65, 90)

# Add data labels
for i, rate in enumerate(df['Retention_Rate']):
    plt.text(i, rate + 0.5, f'{rate:.2f}', 
             ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig('retention_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

# Create bar chart comparison
fig, ax = plt.subplots(figsize=(10, 6))
x = range(len(df))
width = 0.35

bars1 = ax.bar([i - width/2 for i in x], df['Retention_Rate'], 
               width, label='Actual', color='#2E86AB')
bars2 = ax.bar([i + width/2 for i in x], df['Industry_Target'], 
               width, label='Target', color='#A23B72', alpha=0.7)

ax.set_xlabel('Quarter')
ax.set_ylabel('Retention Rate (%)')
ax.set_title('Quarterly Performance vs Industry Target')
ax.set_xticks(x)
ax.set_xticklabels(df['Quarter'])
ax.legend()

# Add value labels
for bar in bars1:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.5,
            f'{height:.2f}', ha='center', va='bottom')

plt.tight_layout()
plt.savefig('quarterly_comparison.png', dpi=300)
plt.show()
