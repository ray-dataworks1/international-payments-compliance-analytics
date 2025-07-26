{% macro sanitise_text(column) -%}
    INTL_PAYMENTS_COMPLIANCE.STAGING.remove_emojis(trim(coalesce({{ column }}, 'unknown')))
{%- endmacro %}