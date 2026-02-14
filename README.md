Senior QA Automation Assessment

This repository contains the automated test suite for the E-commerce platform assignment. It is designed with a "Signal > Coverage" mindset to ensure critical business flows are protected.

## 🛠 Tech Stack & Approach
- **Language:** Python 3.10+
- **Framework:** Playwright (Pytest-based)
- [cite_start]**Why Playwright?** We chose Playwright for its superior auto-waiting capabilities and stability, which effectively mitigate flaky tests in fast-moving environments[cite: 14, 84].
- **Testing Strategy:** A hybrid approach. We use UI-level automation for core user journeys (Login, Add to Cart) to ensure purchase intent is trackable[cite: 13, 83].

## 🚀 How to Run Tests (Docker)
This project is fully containerized to allow consistent execution.

1. **Build and Run:**
   ```bash
   docker compose up --build
View Report: After execution, a report.html will be generated in the project root directory.

📋 Critical Test Scenarios (Section A2)
We focus on these high-impact flows:

Login (Happy Path): Valid user can access the inventory.

Invalid Login: Proper error handling for incorrect credentials.

Find & Add to Cart: Search/Browse for a product and successfully add to cart.

Cart Content Verification: Ensure quantity, name, and price accuracy within the cart.

Cart Persistence: Verify that items remain in the cart after a page refresh.

🏗 Test Architecture & Leadership (Section B/D)

Flaky Prevention (B2): We utilize Playwright's expect auto-wait assertions and dynamic data seeding to maintain isolation and stability.


What NOT to Automate (D1): We intentionally skip visual "pixel-perfect" layout tests and third-party payment gateways, favoring manual monitoring for these low-ROI or high-volatility areas.
