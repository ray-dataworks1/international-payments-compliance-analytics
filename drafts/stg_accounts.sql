-- with raw as (
--     select
--     *
--     from {{ source('raw', 'accounts') }}
-- ),

-- sanitised as (
--     select 
--         id,
--         account_number,
--         customer_id,
--         country_code,
--         is_active,
--         created_at),
    