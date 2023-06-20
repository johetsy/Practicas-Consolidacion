--FINAL MODULO 5 JOHETSY ALVAREZ---
--Construye las siguientes consultas:
--•	Aquellas usadas para insertar, modificar y eliminar un “Customer”,” Staff” y “Actor”. 

--CUSTOMER--
insert into customer (store_id,first_name,last_date,email,address_id,activebool,create_date,last_update,active)
values (1,'Juana','Perez','jperez@gmail.com',606,true,'2023-06-01','2023-06-01 12:36:57.62')

update customer
set last_name = 'Gonzalez',email='jgonzalez@gmail.com'
where customer_id = 601

delete from customer
where customer_id =601

--STAFF--
insert into staff (first_name,last_name,address_id,email,store_id,active,username,password,last_update,picture)
values ('Camila','Perez',5,'cperez@gmail.com',1,true,'Cami','123456789123456789123456','2023-06-01 12:36:57.79328')

update staff
set email='camila.perez@hotmail.com'
where staff_id = 3

delete from staff
where staff_id =3

--ACTOR--
insert into actor (first_name,last_name,last_update)
values ('Pedro','Perez','2023-05-26 11:55:57.62')

update actor
set first_name ='James'
where actor_id = 201

delete from actor
where actor_id =201

--•	Listar todas las “rental” con los datos del “customer” dado un año y mes. 

inner join customer 
on rental.customer_id = customer.customer_id 
where DATE_PART('YEAR', rental_date) = 2005 AND
      DATE_PART('MONTH', rental_date) = 07 
order by rental_date


--•	Listar Número, Fecha (payment_date) y Total (amount) de todas las “payment”. 

SELECT CAST(payment_date AS DATE) AS fecha, SUM(amount) as total_amount    
FROM payment
GROUP BY CAST(payment_date AS DATE)
ORDER BY CAST(payment_date AS DATE)


--•	Listar todas las “film” del año 2006 que contengan un (rental_rate) mayor a 4.0. 
select film_id, title, release_year, rental_rate
from film
where release_year = 2006 and rental_rate > 4.0
group by film_id, title, release_year, rental_rate
order by rental_rate asc

