# Data Profiling Summary


**ELI5: What do these columns mean?**
- **Data Type:** What kind of data is in this column? (numbers, text, dates, True/False, etc.)
- **Non-Null Count:** How many rows have *something* in this column? (Not empty)
- **Unique Values:** How many different values are there in this column?
- **Missing Values:** How many rows are blank/missing in this column?
- **Missing Percentage:** What percent of the rows are missing/blank?
- **Min/Max/Mean/Std:** Only for number columns—smallest/largest, average, and how much the numbers vary.


---
## Accounts

| Column | Data Type | Non-Null Count | Unique Values | Missing Values | Missing % |
|--------|-----------|---------------|---------------|---------------|-----------|
| id | int64 | 208 | 208 | 0 | 0.00 |
| account_number | object | 206 | 205 | 2 | 0.96 |
| customer_id | object | 198 | 70 | 10 | 4.81 |
| country_code | object | 204 | 6 | 4 | 1.92 |
| is_active | bool | 208 | 2 | 0 | 0.00 |
| created_at | object | 208 | 208 | 0 | 0.00 |

**Numeric column stats:**

| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| id | 208.0 | 104.50 | 60.19 | 1.00 | 52.75 | 104.50 | 156.25 | 208.00 |

**What you need to know (ELI5):**
- 'id' is unique—likely a primary key.
- 'country_code' is a categorical field with a small number of distinct values.
- 'created_at' is unique—likely a primary key.

---
## Compliance_checks

| Column | Data Type | Non-Null Count | Unique Values | Missing Values | Missing % |
|--------|-----------|---------------|---------------|---------------|-----------|
| id | int64 | 307 | 307 | 0 | 0.00 |
| transaction_id | object | 300 | 208 | 7 | 2.28 |
| check_type_id | int64 | 307 | 6 | 0 | 0.00 |
| passed | object | 285 | 3 | 22 | 7.17 |
| checked_at | object | 307 | 307 | 0 | 0.00 |
| notes | object | 264 | 63 | 43 | 14.01 |
| checked_by | object | 262 | 51 | 45 | 14.66 |

**Numeric column stats:**

| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| id | 307.0 | 154.00 | 88.77 | 1.00 | 77.50 | 154.00 | 230.50 | 307.00 |
| check_type_id | 307.0 | 3.33 | 1.69 | 1.00 | 2.00 | 3.00 | 5.00 | 6.00 |

**What you need to know (ELI5):**
- 'id' is unique—likely a primary key.
- 'passed' is a categorical field with a small number of distinct values.
- 'checked_at' is unique—likely a primary key.

---
## Compliance_check_types

| Column | Data Type | Non-Null Count | Unique Values | Missing Values | Missing % |
|--------|-----------|---------------|---------------|---------------|-----------|
| id | int64 | 6 | 6 | 0 | 0.00 |
| check_type | object | 6 | 6 | 0 | 0.00 |

**Numeric column stats:**

| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| id | 6.0 | 3.50 | 1.87 | 1.00 | 2.25 | 3.50 | 4.75 | 6.00 |

**What you need to know (ELI5):**
- 'id' is unique—likely a primary key.
- 'check_type' is unique—likely a primary key.
- 'check_type' is a categorical field with a small number of distinct values.

---
## Countries

| Column | Data Type | Non-Null Count | Unique Values | Missing Values | Missing % |
|--------|-----------|---------------|---------------|---------------|-----------|
| id | int64 | 5 | 5 | 0 | 0.00 |
| code | object | 5 | 5 | 0 | 0.00 |
| name | object | 5 | 5 | 0 | 0.00 |

**Numeric column stats:**

| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| id | 5.0 | 3.00 | 1.58 | 1.00 | 2.00 | 3.00 | 4.00 | 5.00 |

**What you need to know (ELI5):**
- 'id' is unique—likely a primary key.
- 'code' is unique—likely a primary key.
- 'code' is a categorical field with a small number of distinct values.
- 'name' is unique—likely a primary key.
- 'name' is a categorical field with a small number of distinct values.

---
## Currencies

| Column | Data Type | Non-Null Count | Unique Values | Missing Values | Missing % |
|--------|-----------|---------------|---------------|---------------|-----------|
| id | int64 | 9 | 9 | 0 | 0.00 |
| code | object | 9 | 9 | 0 | 0.00 |
| name | object | 9 | 9 | 0 | 0.00 |

**Numeric column stats:**

| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| id | 9.0 | 5.00 | 2.74 | 1.00 | 3.00 | 5.00 | 7.00 | 9.00 |

**What you need to know (ELI5):**
- 'id' is unique—likely a primary key.
- 'code' is unique—likely a primary key.
- 'code' is a categorical field with a small number of distinct values.
- 'name' is unique—likely a primary key.
- 'name' is a categorical field with a small number of distinct values.

---
## Customers

| Column | Data Type | Non-Null Count | Unique Values | Missing Values | Missing % |
|--------|-----------|---------------|---------------|---------------|-----------|
| id | int64 | 70 | 70 | 0 | 0.00 |
| full_name | object | 70 | 62 | 0 | 0.00 |
| dob | object | 70 | 70 | 0 | 0.00 |
| address | object | 67 | 56 | 3 | 4.29 |
| phone_number | object | 66 | 64 | 4 | 5.71 |
| bvn | object | 41 | 36 | 29 | 41.43 |
| nin | object | 35 | 32 | 35 | 50.00 |
| country_of_residence | object | 70 | 6 | 0 | 0.00 |
| kyc_status | object | 39 | 4 | 31 | 44.29 |
| created_at | object | 70 | 70 | 0 | 0.00 |

**Numeric column stats:**

| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| id | 70.0 | 35.50 | 20.35 | 1.00 | 18.25 | 35.50 | 52.75 | 70.00 |

**What you need to know (ELI5):**
- 'id' is unique—likely a primary key.
- 'dob' is unique—likely a primary key.
- **WARNING:** 'bvn' is 41.4% missing.
- **WARNING:** 'nin' is 50.0% missing.
- 'country_of_residence' is a categorical field with a small number of distinct values.
- **WARNING:** 'kyc_status' is 44.3% missing.
- 'created_at' is unique—likely a primary key.

---
## Exchange_rates

| Column | Data Type | Non-Null Count | Unique Values | Missing Values | Missing % |
|--------|-----------|---------------|---------------|---------------|-----------|
| id | int64 | 110 | 110 | 0 | 0.00 |
| from_currency | object | 107 | 10 | 3 | 2.73 |
| to_currency | object | 108 | 9 | 2 | 1.82 |
| rate | float64 | 110 | 110 | 0 | 0.00 |
| valid_from | object | 110 | 110 | 0 | 0.00 |
| valid_to | object | 110 | 110 | 0 | 0.00 |

**Numeric column stats:**

| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| id | 110.0 | 55.50 | 31.90 | 1.00 | 28.25 | 55.50 | 82.75 | 110.00 |
| rate | 110.0 | 693.49 | 379.19 | 19.90 | 363.85 | 725.12 | 1034.85 | 1294.71 |

**What you need to know (ELI5):**
- 'id' is unique—likely a primary key.
- 'to_currency' is a categorical field with a small number of distinct values.
- 'valid_from' is unique—likely a primary key.
- 'valid_to' is unique—likely a primary key.

---
## Remittance

| Column | Data Type | Non-Null Count | Unique Values | Missing Values | Missing % |
|--------|-----------|---------------|---------------|---------------|-----------|
| id | int64 | 213 | 213 | 0 | 0.00 |
| origin_country | object | 199 | 6 | 14 | 6.57 |
| destination_country | object | 198 | 6 | 15 | 7.04 |
| status | object | 213 | 4 | 0 | 0.00 |
| exchange_rate_id | object | 202 | 93 | 11 | 5.16 |
| remittance_method | object | 170 | 6 | 43 | 20.19 |
| created_at | object | 213 | 213 | 0 | 0.00 |

**Numeric column stats:**

| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| id | 213.0 | 107.00 | 61.63 | 1.00 | 54.00 | 107.00 | 160.00 | 213.00 |

**What you need to know (ELI5):**
- 'id' is unique—likely a primary key.
- 'origin_country' is a categorical field with a small number of distinct values.
- 'destination_country' is a categorical field with a small number of distinct values.
- 'status' is a categorical field with a small number of distinct values.
- **WARNING:** 'remittance_method' is 20.2% missing.
- 'created_at' is unique—likely a primary key.

---
## Transactions

| Column | Data Type | Non-Null Count | Unique Values | Missing Values | Missing % |
|--------|-----------|---------------|---------------|---------------|-----------|
| id | int64 | 255 | 255 | 0 | 0.00 |
| amount | float64 | 255 | 157 | 0 | 0.00 |
| currency | object | 242 | 10 | 13 | 5.10 |
| payee_id | object | 242 | 149 | 13 | 5.10 |
| payer_id | object | 239 | 145 | 16 | 6.27 |
| transaction_date | object | 255 | 247 | 0 | 0.00 |
| status | object | 255 | 4 | 0 | 0.00 |
| is_complete | bool | 255 | 2 | 0 | 0.00 |
| created_at | object | 255 | 247 | 0 | 0.00 |
| updated_at | object | 255 | 247 | 0 | 0.00 |
| remittance_id | object | 242 | 142 | 13 | 5.10 |
| exchange_rate_id | object | 242 | 101 | 13 | 5.10 |

**Numeric column stats:**

| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| id | 255.0 | 437.85 | 1748.80 | 1.00 | 64.50 | 128.00 | 191.50 | 10225.00 |
| amount | 255.0 | 3056.45 | 5631.44 | -986.26 | -175.96 | 0.00 | 4731.98 | 19953.85 |

**What you need to know (ELI5):**
- 'id' is unique—likely a primary key.
- 'status' is a categorical field with a small number of distinct values.

---