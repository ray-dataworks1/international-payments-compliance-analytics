You are a senior data engineer at a global cross-border fintech.
Your task is to generate a hyper-realistic, messy, and audit-ready synthetic dataset for an international payments compliance analytics MVP.
The schema and relationships are explicitly detailed below.
Your dataset must simulate the regional, diaspora, and dirty-data quirks found in a real-world Lemfi/WorldRemit/Wise warehouse.

Schema & Relationships
Entities/Tables
Countries (id, code, name)

Currencies (id, code, name)

Customers (id, full_name, dob, address, phone_number, bvn, nin, country_of_residence, kyc_status, created_at)

Accounts (id, account_number, customer_id, country_code, is_active, created_at)

Exchange_rates (id, from_currency, to_currency, rate, valid_from, valid_to)

Remittance (id, origin_country, destination_country, status, exchange_rate_id, remittance_method, created_at)

Transactions (id, amount, currency, payee_id, payer_id, transaction_date, status, is_complete, created_at, updated_at, remittance_id, exchange_rate_id)

Compliance_check_types (id, check_type)

Compliance_checks (id, transaction_id, check_type_id, passed, checked_at, notes, checked_by)

See PlantUML ERD below for foreign key relationships:

plantuml
Copy
Edit
@startuml
entity Countries {
* id : serial
---
* code : varchar(3)
* name : varchar(50)
}
entity Currencies {
 * id : serial
 ---
 * code : varchar(3)
 * name : varchar(50)
 }
 entity compliance_check_types {
 * id : serial
 * check_type : varchar(50)
 }
 entity Customers {
 * id : serial
 ---
 * full_name : varchar(100)
 * dob : date
 * address : varchar(255)
 * phone_number : varchar(30)
 * bvn : varchar(20)
 * nin : varchar(20)
 * country_of_residence : varchar(3) (FK to Countries)
 * kyc_status : varchar(20)
 * created_at : timestamp with time zone
 }
 Countries ||---{ Customers
 entity Accounts {  
 * id : serial
 ---
 * account_number: varchar(50)
 * customer_id : integer (FK to Customers)
 * country_code : varchar(3) (FK to Countries)
 * is_active : bool
 * created_at : timestamp with time zone
 }
 Customers ||--{ Accounts
 Countries ||--{ Accounts
 entity exchange_rates {
 * id : serial
 ---
 * from_currency : varchar(3) (FK to Currencies)
 * to_currency : varchar(3) (FK to Currencies)
 * rate : numeric(12,6)
 * valid_from : timestamp with time zone
 * valid_to : timestamp with time zone
 }
 Currencies ||--{ exchange_rates
 entity Remittance {
 * id : serial
 ---
 * origin_country : varchar(3) (FK to Countries)
 * destination_country : varchar(3) (FK to Countries)
 * status : varchar(20)
 * exchange_rate_id : integer (FK to exchange_rates)
 * remittance_method : varchar(50)
 * created_at : timestamp with time zone
 }
 Countries ||---{ Remittance
 exchange_rates }--|| Remittance
 entity Transactions {
 * id : serial
 * amount : numeric(12,2)
 * currency : varchar(3) (FK to Currencies)
 * payee_id : integer (FK to Accounts)
 * payer_id : integer (FK to Accounts)
 * transaction_date : timestamp with time zone
 * status : varchar(20)
 * is_complete : bool
 * created_at : timestamp with time zone
 * updated_at : timestamp with time zone
 * remittance_id : integer (FK to Remittance)
 * exchange_rate_id : integer (FK to exchange_rates)
 }
 Accounts ||--{ Transactions
 Currencies ||--{ Transactions
 Remittance ||--{ Transactions
 entity compliance_checks {
 * id : serial
 ---
 * transaction_id : integer (FK to Transactions)
 * check_type_id : integer (FK to compliance_check_types)
 * passed : bool
 * checked_at : timestamp with time zone
 * notes : text
 * checked_by : varchar(50)
 }
 compliance_checks ||--|| compliance_check_types
 Transactions ||--{ compliance_checks
@enduml
Dataset Requirements
Countries & Currencies
At least 5: UK, US, Nigeria, France (or Eurozone), China.

Include both ISO and dirty/nonstandard codes (e.g., UK, NG, EURO, YUAN).

Customers
Name & Nationality Realism:

Nigeria (NGA/NG): All names authentically Nigerian (Yoruba, Igbo, Hausa, etc), realistic Naija addresses.

UK/US/France/China:

Majority of customers have region-typical names (e.g. British, American, French, Chinese).

Minority (e.g. 10–20%) have plausible diaspora names (Nigerian, West African, South Asian, Arab, Polish, etc), reflecting real-world diversity.


Some names/addresses should be corrupted, incomplete, or contain non-ASCII, emoji, etc.

Phone numbers: Realistic per country (+234, +44, +1, +33, +86) and you have to assign them to each case according to the country code, but some invalid/truncated/duplicate.

BVN/NIN: Present for Nigerians and Naija diaspora (occasionally missing/dirty).

KYC: PASSED, FAILED, PENDING, FLAGGED, with random messiness/incompleteness.

Dirty data: About 5–10% should be incomplete, corrupted, or orphaned.

Accounts
1–5 per customer, may be in different countries, some duplicates/incomplete/missing.

Some inactive/missing/dirty FKs.

Exchange Rates
Overlapping validity, missing/dirty codes, gaps.

Remittance
Real corridors (NGN→USD/GBP/EUR, GBP/USD→NGN, etc.), messy country/currency codes, mix of methods.

Transactions
Local & cross-border, edge cases: zero/negative/rounded/large/small, batch, out-of-order, missing/mismatched FKs, duplicate/dirty.

Compliance Checks
Types: AML Threshold, PEP Screening, Sanctions List, KYC Check, Geo IP Mismatch, Manual Review.

Notes: Officer/system-generated, including "BVN mismatch", "KYC doc expired", "Transaction flagged", "SAR filed", "Name mismatch", "OFAC checked", "Passport expired", "NIN not found", blanks, dashes, emoji, messy, truncated.

Checked_by: Officer names (regionally appropriate), emails, system users/bots, empty.

Dates
2 years in past to 30 days in future, out-of-order, batch, etc.

Volume
30–80 customers, 100–500 transactions, 5–15 accounts per country, others scaled.

Output
Return Python code (Pandas code or CSVs) for each table, fully relational, with comments explaining data-generation, edge cases, and messiness logic.

Diaspora/Nationality Logic for Names
For each UK/US/FR/CHN customer:

With 80–90% probability, assign a region-typical name.

With 10–20% probability, assign a plausible diaspora name (African, South Asian, Arab, Polish, etc.), matching real demographics.

For Nigerians, always generate Nigerian names.

Phone numbers, addresses, and BVN/NIN should match the regional logic above.

Goal
The goal is to create a dataset as globally diverse, messy, and realistic as what is actually ingested by a cross-border payments/fintech company—full of the same real-world quirks, dirty data, edge cases, and auditability requirements.

Deliverable
Return ONLY the Python code to generate the CSVs for each table, using the schema and requirements above.
Include concise comments to explain how regionalization, dirty data, edge cases, and relationships were handled. For faker, there is no faker_ng library, so please handle this edge case.

This prompt is ready for direct copy + paste for advanced mock data generation or code LLMs.
It is optimised for both compliance analytics and realistic data engineering upskilling use-cases.