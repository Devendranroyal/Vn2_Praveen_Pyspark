CREATE EXTERNAL TABLE store_day_sale_t(
     Store_id INT,
     Store_code STRING,
     Sale_Date STRING,
     Sale_Amount INT)
 ROW FORMAT DELIMITED 
 FIELDS TERMINATED BY ','
 LINES TERMINATED by '\n'
 LOCATION '/user/HADOOP/E0exercise/hivefiles/external';

-- load data inpath './E0exercise/hivefiles/sale_data.dat' overwrite into table store_day_sale_t;


create table store_week_sale_t as
select store_id,
       store_code,
       concat(year(sale_date),weekofyear(sale_date)) as sale_week,
       sum(sale_amount) as week_sale_amt
from store_day_sale_t
group by store_id,
       store_code,
       concat(year(sale_date),weekofyear(sale_date));



