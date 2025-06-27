# International Payments Compliance Analytics MVP
**Tech Stack:** Snowflake | dbt | Python (Pandas) | Looker

## 🚀 Project Overview

This repo demonstrates a modern Analytics Engineering workflow for compliance and business reporting in cross-border fintech, inspired by LemFi’s mission. It simulates transaction monitoring and compliance analytics using a cloud-native pipeline:  
- `Snowflake` (data warehouse)  
- `dbt` (transformations, documentation, testing)  
- `Python/Pandas` (data preprocessing, seeding)
- `ChatGPT` (realistic, efficient mock data creation)
- `Looker` (BI dashboarding and stakeholder comms)

## Business Problem

> As any FinTech scales global payments, robust, automated compliance analytics are vital. This MVP models how flagged transactions and regulatory KPIs can be surfaced for Compliance and Business teams—reducing risk, improving auditability, and driving better decisions.

## Stack & Architecture

- **Snowflake:** Stores raw and modeled transaction data for high scalability and security.
- **dbt:** Handles SQL-based transformations, documentation, lineage, and tests (e.g., suspicious activity, compliance KPIs).
- **Python (Pandas):** Preps and seeds realistic synthetic data (CSV ➡️ Snowflake).
- **Looker:** Surfaces key metrics via interactive dashboards (e.g., flagged transactions, volume by corridor/country, trend analysis).

## Project Structure

international-payments-compliance-analytics/
├── data/                # Seed/simulated datasets
│   └── transactions.csv
├── dbt/
│   ├── models/
│   │   ├── staging/
│   │   └── marts/
│   └── tests/
├── scripts/
│   └── seed_snowflake.py  # Python: loads seed data
├── looker/
│   └── dashboard_screenshots/
├── README.md
└── .gitignore

### Key Features
Flagged Transactions: Automated logic to detect KYC/AML red flags (thresholds, unusual behavior).

Compliance KPIs: Number/percent of flagged transactions, transaction volumes by corridor, new vs. returning users.

End-to-End Pipeline: From CSV seed → Snowflake (raw) → dbt (modeled) → Looker (dashboard).

Documentation: dbt docs, entity diagrams, test coverage, data lineage.

### How to Run

#### Install Requirements:

Python 3.x, dbt (with Snowflake adapter), Snowflake account, Looker (demo or sandbox).

pip install -r requirements.txt (for Pandas etc.)

Load Seed Data

Edit scripts/seed_snowflake.py with your Snowflake creds.

Run: python scripts/seed_snowflake.py

Run dbt Models

Edit dbt/profiles.yml for your Snowflake connection.

cd dbt

dbt run

dbt test

Dashboard

Import dbt models as Looker views.

Use included LookML or screenshots for demo if sandbox not available.

### Business Impact
Risk Reduction: Near real-time compliance visibility

Scalability: Modular, repeatable analytics pipeline (cloud-first)

Clarity: Single source of truth for BI, stakeholder-ready

🎤 Author
Rachael Ogungbose
Junior Data Analytics Engineer | Fintech, Compliance, Cloud
2nd-gen immigrant based in the UK, passionate about systems, equity, and financial empowerment for immigrant communities.
