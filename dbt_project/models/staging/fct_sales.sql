
with source as (
    select * from {{ source('main', 'fct_sales') }}
)

select
    sales_id,
    hco_id,
    product,
    qty,
    cast(sales_date as date) as sales_date
from source
