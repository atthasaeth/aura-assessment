# AI Prompts & Assistance Log

This document details how AI tools were utilized to accelerate the development of this test suite

## Exact Prompts Used
1. **Scaffolding:** "Generate a Python Playwright test using Pytest for an e-commerce login and add-to-cart flow."
2. **Containerization:** "Create a Dockerfile and docker-compose.yml for running Python Playwright tests in a Ubuntu-based container."

## AI Acceleration
- **Speed:** AI significantly reduced the time required to write boilerplate code for Page Object models and Docker configurations
- **Logic Refinement:** AI assisted in drafting the initial Automation Strategy based on the provided scenario

## Validations & Rejections
- **Manual Refactoring:** AI initially suggested using generic CSS selectors (e.g., `.btn-primary`). I rejected these in favor of `get_by_role` or `get_by_placeholder` for better resilience
- **Correctness Check:** Every script was dry-run locally to ensure assertions accurately reflect the System Under Test (SUT)
- **Docker Fix:** AI provided an older Docker image version. I manually updated it to `v1.58.0-jammy` to match the latest Playwright library version.