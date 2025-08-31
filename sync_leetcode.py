name: Sync LeetCode Solutions

on:
  schedule:
    - cron: '0 6 * * *'   # Runs daily at 6 AM UTC
  workflow_dispatch:      # Allow manual trigger

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: pip install requests

      - name: Run sync script
        run: python sync_leetcode.py

      - name: Commit & Push changes
        run: |
          git config --global user.name "GitHub Actions"
          git config --global user.email "actions@github.com"
          git add .
          git commit -m "Update LeetCode solutions"
          git push
