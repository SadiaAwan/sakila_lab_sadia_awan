select
  c.customer_id,
  c.first_name || ' ' || c.last_name as customer_name,
  sum(p.amount) as total_spend
from customer c
join staging.payment p on c.customer_id = p.customer_id
group by c.customer_id, customer_name
order by total_spend DESC;

