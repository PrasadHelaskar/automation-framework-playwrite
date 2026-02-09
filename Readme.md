# 🚀 Automation Framework — Playwright

![Build Status](https://img.shields.io/badge/build-in_progress-yellow)
![Test Status](https://img.shields.io/badge/tests-active-blue)
![Coverage](https://img.shields.io/badge/coverage-planned-lightgrey)
![Framework Stage](https://img.shields.io/badge/framework-phase--1-orange)
![Continuous Development](https://img.shields.io/badge/continuous-development-brightgreen)

---

## 📌 About

A scalable, maintainable, and modular **Playwright Automation Framework** built using **Python + Pytest** for modern Web UI end-to-end testing.

This repository represents a **production-style automation framework**, developed incrementally using a **continuous, phased engineering approach** rather than a one-time demo implementation.

The framework is designed with long-term maintainability, clarity, and scalability in mind — closely mirroring how automation systems evolve in real-world QA teams.

---

## ✨ Key Features

✔ Playwright-based UI automation using Python </br>
✔ Page Object Model (POM) architecture </br>
✔ Centralized locator management </br>
✔ Pytest fixtures and configuration </br>
✔ Reusable utilities and base classes </br>
✔ CLI-driven test execution </br>
✔ Framework designed for CI/CD readiness </br>

---

## 📁 Project Structure

```
.
├── locatores/            # Centralized UI locators
├── pages/                # Page Object Models
├── tests/                # Test cases grouped by feature
├── utils/                # Common utilities (logger, helpers, base logic)
├── conftest.py           # Pytest fixtures and setup/teardown
├── pytest.ini            # Pytest configuration & markers
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 🛠 Prerequisites

* Python 3.8+
* Node.js (required for Playwright browsers)
* pip

### Install dependencies

```bash
pip install -r requirements.txt
```

### Install Playwright browsers

```bash
playwright install
```

---

## ▶️ Running Tests

Run all tests:

```bash
pytest
```

Run with verbose logs:

```bash
pytest -v
```

Run a specific test or folder:

```bash
pytest tests/
pytest tests/login/test_login.py
```

---

## 🔄 Continuous Development (Phased Approach)

This framework follows a **phased continuous development strategy**, ensuring that each stage delivers stable and usable automation while allowing controlled growth.

### 🟠 Phase 1 — Foundation (Current)

✔ Project structure finalized </br>
✔ Playwright + Pytest integration </br>
✔ Page Object Model (POM) </br>
✔ Centralized locator strategy </br>
✔ BasePage abstraction for UI interactions </br>
✔ Reusable utilities </br>

🎯 **Objective:** Establish a clean, maintainable automation baseline.

---

### 🔵 Phase 2 — Stabilization & Coverage (Planned)

⬜ Test data management </br>
⬜ Assertion helpers </br>
⬜ HTML / Allure reporting </br>
⬜ Enhanced logging & failure analysis </br>
⬜ Smoke vs Regression tagging </br>

🎯 **Objective:** Improve reliability, diagnostics, and test visibility.

---

### 🟢 Phase 3 — CI/CD & Scalability (Upcoming)

⬜ GitHub Actions CI pipeline </br>
⬜ Parallel execution </br>
⬜ Cross-browser execution strategy </br>
⬜ Environment-based execution (test / staging / prod) </br>

🎯 **Objective:** Make the framework CI-ready and production-scalable.

---

### 🔮 Phase 4 — Advanced Automation (Future)

⬜ Self-healing locators </br>
⬜ Flaky test detection </br>
⬜ Visual regression testing </br>
⬜ API + UI hybrid automation flows </br>

🎯 **Objective:** Transition from automation execution to automation intelligence.

---

## 🧠 Engineering Philosophy

* Built as a **living framework**, not a one-time implementation
* Each phase adds value without breaking existing tests
* Emphasis on readability, maintainability, and scalability
* Mirrors real-world SDET automation practices

---

## 📈 Framework Versioning

**Current Version:** `v1.0`

* Foundation phase completed
* Stable baseline for further enhancements

Future versions will increment as each phase is completed.

---

## 🤝 Contributions

Suggestions, issues, and improvements are welcome.

This framework is intentionally designed to evolve — contributions that align with the phased roadmap are encouraged.

---

## 👤 Author

Prasad Helaskar
Senior QA / SDET (Automation) </br>
🔗 GitHub: https://github.com/PrasadHelaskar

> 📢 *This repository reflects how real automation frameworks are built, evolved, and maintained in professional QA organizations.*
