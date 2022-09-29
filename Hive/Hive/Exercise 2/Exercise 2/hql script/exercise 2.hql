CREATE TABLE store_info_t(
     Store_id INT,
     Store_city STRING,
     Store_name STRING)
 ROW FORMAT DELIMITED
 FIELDS TERMINATED BY ','
 LINES TERMINATED BY '\n';


load data inpath './E0exercise/hivefiles/store_detail.dat' overwrite into table store_info_t;

-- equi join

select a.store_id,
       a.store_code,
       a.sale_week,
       b.store_city,
       b.store_name,
       a.week_sale_amt
  from store_week_sale_t  a 
       join 
       store_info_t b on
a.store_id = b.store_id 
sort by a.sale_week,a.store_id;


-- left outer join

select a.store_id,
       a.store_code,
       a.sale_week,
       b.store_city,
       b.store_name,
       a.week_sale_amt
  from store_week_sale_t  a 
  left outer join 
       store_info_t b on
a.store_id = b.store_id 
sort by a.sale_week,a.store_id;


-- right outer join.

select a.store_id,
       a.store_code,
       a.sale_week,
       b.store_city,
       b.store_name,
       a.week_sale_amt
  from store_week_sale_t  a 
  right outer join 
       store_info_t b on
a.store_id = b.store_id 
sort by a.sale_week,a.store_id;


-- left semi join


select a.store_id,
       a.store_code,
       a.sale_week,
       a.week_sale_amt
  from store_week_sale_t  a 
  left semi join 
       store_info_t b on
a.store_id = b.store_id;


