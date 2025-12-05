# PR_INSTRUCTIONS.md

Steps to produce a GitHub Pull Request containing this analysis (run locally):

1. Unzip and navigate into the package, or clone your repo and copy files into it.
2. Create and switch to a new branch for the PR:
   ```bash
   git checkout -b feat/retention-analysis-jules-codex
   ```
3. Stage files and commit with LLM-labeled commits:
   ```bash
   git add .
   git commit -m "chore(data): add retention dataset and analysis script — Jules (ChatGPT Codex)"
   git commit -m "feat(analysis): generate retention trend plot and summary — Jules (ChatGPT Codex)"
   ```
   (Two commits shown to make LLM assistance visible in history. You can also squash if you prefer.)
4. Push the branch to your GitHub remote (replace `origin` and branch as needed):
   ```bash
   git push origin feat/retention-analysis-jules-codex
   ```
5. On GitHub, open a Pull Request from `feat/retention-analysis-jules-codex` into your main branch.
   - PR title suggestion: `feat: add retention analysis & recommendations — Jules (ChatGPT Codex)`
   - PR description suggestion (copy into GitHub PR description box):\n
   ```
   This PR adds a small LLM-assisted analysis of 2024 customer retention (quarterly data and visualization),
   includes the recommended solution to implement targeted retention campaigns, and provides actionable recommendations.
   Author verification email: 24ds2000078@ds.study.iitm.ac.in
   Reported average (per assignment): 71.61
   LLM assistance noted in commits: Jules (ChatGPT Codex)
   ```
6. After creating the PR, attach `outputs/retention_trend.png` in the repo (the file is already included in this package if you ran the script locally).

Expected outcome: your PR will contain analysis code, visual(s), README with data story, LLM-labeled commits, and the verification email as required.
