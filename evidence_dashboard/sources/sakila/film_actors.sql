select
    f.title,
    f.rating,
    a.first_name || ' ' ||  a.last_name AS actor
from
    staging.film f
    left join staging.film_actor fa on fa.film_id = f.film_id
    left join staging.actor a on a.actor_id = fa.actor_id