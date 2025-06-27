# Use Case + Business Question Definition
The goal of this dataset and the subsequent staging, intermediate and mart models is to enable compliance reporting for remittances and global transactions in Snowflake, supporting stakeholder queries.

```plantuml
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
```
