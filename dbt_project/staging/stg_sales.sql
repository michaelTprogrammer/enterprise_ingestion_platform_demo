-- staging model
select * from {{ source('main', 'fct_sales') }}
