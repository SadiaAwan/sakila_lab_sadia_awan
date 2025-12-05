# EDA sakila

Full film data here:

```sql films
from sakila.film
```

```sql topmost_5_clients
select
  c.customer_id,
  c.first_name || ' ' || c.last_name as customer_name,
  sum(p.amount) as total_spend
from sakila.customer c
join payment p on c.customer_id = p.customer_id
group by c.customer_id, customer_name
order by total_spend DESC;



```

Picks out all the films with actors and title with rating G
```sql film_actor
from sakila.film_actors
where rating = 'G';
```

## Number of films in each rating

Data

```sql number_films_by_rating
select
    rating,
    count(film_id) as total_films
from film
group by rating
order by rating
```

<BarChart
    data={number_films_by_rating}
    title="Number of films per rating"
    x=rating
    y=total_films 
    xAxisTitle="rating"
    yAxisTitle="nr of movies" 
/>