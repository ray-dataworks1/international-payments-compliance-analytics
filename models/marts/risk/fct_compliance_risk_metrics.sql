-- fct_compliance_risk_metrics.sql
{{ config(materialized='table') }}

with src as (
  select * from {{ ref('dim_customer_risk_profiles') }}
),
aggregated as (
  select
    current_date() as snapshot_date,
    avg(total_risk_percentage) as avg_total_risk,
    sum(case when total_risk_percentage > 80 then 1 else 0 end) as high_risk_customers,
    sum(case when kyc_status = 'pending' then 1 else 0 end) as kyc_pending,
    sum(case when country_of_residence in ('NG','PK','AF','IR','SY','YE','SD') then 1 else 0 end) as high_risk_country_customers,
    count(*) as total_customers
  from src
)
select *,
       round((high_risk_customers::decimal / total_customers) * 100, 2) as pct_high_risk
from aggregated
