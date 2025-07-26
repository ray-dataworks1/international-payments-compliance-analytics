{% macro generate_schema_name(custom_schema_name, node) -%}
    {#-
        Use the custom_schema_name if provided (e.g. from +schema: in dbt_project.yml).
        Otherwise, fall back to the target schema (from your profiles.yml).
        This prevents dbt default behaviour of combining the two with an underscore!
        Docs: https://docs.getdbt.com/reference/dbt-jinja-functions/generate_schema_name
    -#}
    {{ custom_schema_name if custom_schema_name is not none else target.schema }}
{%- endmacro %}
