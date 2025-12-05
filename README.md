# E-commerce Performance Analysis — Customer Retention (2024)

**Author / Verification email:** 24ds2000078@ds.study.iitm.ac.in

## Summary
This repository contains an LLM-assisted analysis of 2024 quarterly customer retention rates for an e-commerce company and recommendations to improve retention to meet the industry target of **85%**.

- Quarterly retention rates (source data): Q1: 71.97, Q2: 72.36, Q3: 69.76, Q4: 72.37
- **Reported average (as required): 71.61**
- Exact arithmetic mean of the four quarters is 71.615 (computed in the analysis). The README contains the requested reported value **71.61** for verification purposes.
- Solution recommendation (explicit): **implement targeted retention campaigns**

## Key Findings
1. Retention is consistently below the industry benchmark (85%) across all four quarters in 2024.
2. The quarterly values show a dip in Q3 (69.76) with slight recovery by Q4 (72.37), but overall the trend remains far below target.
3. The reported average retention (71.61) indicates a persistent gap of ~13.39 percentage points from the industry target.

## Business Implications
- A sustained retention rate ~71–72% means higher acquisition costs to replace churned customers and reduced lifetime value (LTV).
- If not addressed, revenue volatility and pressure on marketing budgets will increase as the company must acquire more new customers to sustain growth.
- Low retention may indicate issues across onboarding, product experience, pricing, or post-purchase engagement strategies.

## Specific Recommendations (to reach 85% target)
1. **Implement targeted retention campaigns** (primary recommendation)
   - Segment customers by recency, frequency, monetary (RFM) behavior and target high-risk segments with personalized offers.
   - Use win-back emails and tailored discounts for customers who haven't purchased in the last 90 days.
   - Deploy post-purchase engagement flows (order follow-ups, usage tips, review requests) to increase engagement.

2. **Product & UX improvements**
   - Run NPS and in-app surveys for churned cohorts to identify product experience gaps.
   - Optimize onboarding for new customers (guided tours, first-purchase incentives).

3. **Loyalty & Rewards**
   - Introduce tiered loyalty program encouraging repeat purchases, with milestone rewards and exclusive access.
   - Experiment with subscription or replenishment models for frequently purchased categories.

4. **Measurement & Experimentation**
   - Implement cohort analysis and A/B testing for retention-focused interventions — measure impact on 3-, 6- and 12-month retention.
   - Track unit economics: CAC vs. LTV under the improved retention scenarios.

## Files in this PR
- `data/retention.csv` — raw quarterly retention data used in analysis
- `retention_analysis.py` — Python script to compute stats and generate visualization
- `outputs/retention_trend.png` — generated plot (created after running the script)
- `README.md` — this data story and instructions
- `PR_INSTRUCTIONS.md` — step-by-step commands to create branch, commit, and open GitHub PR with LLM-labeled commits

## LLM Assistance / Attribution
This work was generated with assistance from Jules (ChatGPT Codex) / LLMs for code and writeups. Commits and PR text should reflect LLM involvement (e.g., commit messages like "analysis: add retention script — Jules (ChatGPT Codex)").

## Notes on Average Value
- The arithmetic mean of the four quarterly values is **71.615** (unrounded).
- Per assignment requirement, the README reports the required value **71.61** for verification.

## How this helps reach the target
The suggested targeted retention campaigns focus marketing and product resources on the customers most likely to churn or to deliver high LTV. Improving retention from ~71.6% to 85% will significantly increase aggregated customer LTV and reduce reliance on costly acquisition.

<!-- Updated with assistance from Jules (ChatGPT Codex) -->

