with raw as (
    select
    id,
    full_name,
    dob,
    address,
    phone_number,
    bvn,
    nin,
    country_of_residence,
    kyc_status,
    created_at
    from {{ source('raw', 'customers') }}
),
-- deduped as (
--     select
--         *,
--         row_number() over (partition by id order by id desc) as rn
--     from raw
-- ),

sanitised as (
    SELECT
        id as customer_id_raw,
        try_cast(id as integer) as customer_id,
        {{ sanitise_text('full_name') }} as full_name,
        cast(dob as date) as dob,
        {{ sanitise_text('address') }} as address,
        {{ sanitise_text('phone_number') }} as phone_number,
        {{ sanitise_text('bvn') }} as bvn,
        {{ sanitise_text('nin') }} as nin,
        {{ normalise_field('country_of_residence') }} as country_of_residence,
        {{ normalise_field('kyc_status')}} as kyc_status,
        cast(created_at as timestamp) as created_at
        from raw
),

finalised_and_normalised as (
    select 
    *,
    case when address = 'unknown'
    or phone_number = 'unknown'
    or (bvn = 'unknown' and country_of_residence = 'NG')
    or (nin = 'unknown' and country_of_residence = 'NG')
    or country_of_residence = 'unknown'
    or kyc_status = 'unknown'
    then TRUE
    else FALSE
    end as for_review,
    case when customer_id_raw is null then true else false end as id_issue
    from sanitised
)

select
customer_id_raw,
customer_id,
full_name,
dob,
address,
phone_number,
bvn,
nin,
country_of_residence,
kyc_status,
created_at,
for_review,
id_issue
from finalised_and_normalised



