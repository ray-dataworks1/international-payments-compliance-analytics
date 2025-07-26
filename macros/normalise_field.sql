{% macro normalise_field(column) -%}
    upper({{ sanitise_text(column) }})
{%- endmacro %}
