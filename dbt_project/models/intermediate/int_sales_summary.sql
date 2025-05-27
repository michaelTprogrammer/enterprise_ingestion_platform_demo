-- intermediate logic
select hco_id, sum(qty) as total_qty from {{ ref('stg_sales') }} group by hco_id
