with raw as ( 
    select *
    from {{ source('raw', 'accounts') }}
),

sanitised as (
    select 
        id as raw_account_id,
        try_cast(id as integer) as account_id,
        {{ sanitise_text('account_number') }} as account_number,
        {{ normalise_field('country_code') }} as country_code,
        customer_id as customer_id,
        CAST(is_active AS BOOLEAN) as is_active,
        CAST(created_at AS TIMESTAMP) as created_at
    from raw
),
finalised_and_normalised as (
    select raw_account_id,
    account_id,
    account_number,  
    country_code,
    customer_id,
    is_active,
    created_at,
    case when account_number in ('unknown', '-', '?', '—','')
    or not regexp_like(account_number, '^[0-9]{13}$')
    or account_number is null
    or len(account_number) != 13 then true else false end as for_review
    from sanitised
    order by raw_account_id ASC
)
select 
    raw_account_id,
    account_id,
    account_number,
    country_code,
    customer_id,
    is_active,
    created_at,
    for_review
from finalised_and_normalised
