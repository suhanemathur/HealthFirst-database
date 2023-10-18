use healthfirst;

#OLAP 1
#This query gives the product ID and the Total price of which products are available product_price*product_availability
SELECT product.category_ID,manufactures.supplier_ID, SUM(product.product_availability * product.product_price) AS 'Total Price'
FROM product
JOIN manufactures on  product.product_ID = manufactures.product_ID
GROUP BY manufactures.supplier_ID,product.category_ID WITH ROLLUP;




SELECT product_name,product_expiry,Product_id,product_manufacture,supplier_ID
FROM Product join manufactures on product.product_ID=manufactures.product_ID
WHERE product_expiry = (SELECT MIN(product_expiry) FROM Product) 
group by supplier_ID;


SELECT product_ID, COUNT(illness_ID) 
FROM recommends NATURAL JOIN product
WHERE product.product_availability > 100
GROUP BY product_ID,category_ID;

#OLAP Query 4: 
SELECT category_ID, COUNT(product_ID) 
FROM product
GROUP BY category_ID WITH ROLLUP;







SELECT product.category_ID,manufactures.supplier_ID, SUM(product.product_availability * product.product_price) AS 'Total Price'
FROM product
JOIN manufactures on  product.product_ID = manufactures.product_ID
GROUP BY manufactures.supplier_ID,product.category_ID WITH ROLLUP;


select access.admin_ID,order_dispatch.transaction_success,count(access.customer_ID)
from access
join order_dispatch on
access.customer_ID=order_dispatch.customer_ID 
group by access.admin_ID,order_dispatch.transaction_success with rollup;

select recommends.customer_ID,recommends.category_ID,count(recommends.product_ID) 
from recommends 
group by customer_ID,category_ID with rollup;

update recommends set customer_ID=3 where product_id=1;



select YEAR(product_expiry) as year,MONTH(product_expiry) AS month ,category_ID,count(product_id) from product 
where product_availability>100
group by YEAR,MONTH,category_ID with rollup;
