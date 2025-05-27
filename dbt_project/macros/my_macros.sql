
-- Return today's date
{% macro today_date() %}
    cast(current_date as date)
{% endmacro %}

-- Return first day of current month
{% macro first_day_of_month() %}
    date_trunc('month', current_date)
{% endmacro %}

-- Return previous month range
{% macro last_month_range() %}
    {{
        return(
            "date_trunc('month', current_date - interval '1 month') as start_date, "
            "date_trunc('month', current_date) - interval '1 day' as end_date"
        )
    }}
{% endmacro %}
