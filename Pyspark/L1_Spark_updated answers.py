1. What are PySpark serializers?

The serialization process is used to conduct performance tuning on Spark. 
The data sent or received over the network to the memory should be persisted. 
#PySpark supports serializers for this purpose. 
It supports two types of serializers, they are:

PickleSerializer  : This serializes objects using Python’s PickleSerializer 
                    #(class pyspark.PickleSerializer). 
					This supports almost every Python object.
MarshalSerializer : This performs serialization of objects. 
                    #We can use it by using class pyspark.MarshalSerializer. 
					This serializer is faster than the PickleSerializer but supports only limited types.

***********************************************************************************
2. What are the different cluster manager types supported by PySpark?

A cluster manager is a cluster mode platform that helps to run Spark by providing all resources to worker nodes based on the requirements.


PySpark supports the some cluster manager types:

Standalone – This is a simple cluster manager that is included with Spark.
Apache Mesos – This manager can run Hadoop MapReduce and PySpark apps.
Hadoop YARN – This manager is used in Hadoop2.
Kubernetes – This is an open-source cluster manager that helps in automated deployment, scaling and automatic management of containerized apps.
local – This is simply a mode for running Spark applications on laptops/desktops.
**********************************************************************************
call kalyan only
17. What is PySpark Architecture?
PySpark is similar to Apache Spark which works in master-slave architecture pattern. 
Here, the master node is called the Driver and the slave nodes are called the workers. 
When a Spark application is run, the Spark Driver creates SparkContext which acts as an entry point to the spark application. 
All the operations are executed on the worker nodes. 
The resources required for executing the operations on the worker nodes are managed by the Cluster Managers

*****************************************************************************************
18. What PySpark DAGScheduler?
DAG stands for Direct Acyclic Graph. 
It constitutes the scheduling layer of Spark which implements scheduling of tasks in a stage-oriented manner using jobs and stages. 
The logical execution plan (Dependencies lineage of transformation actions upon RDDs) is transformed into a physical execution plan consisting of stages. 
It computes a DAG of stages needed for each job and keeps track of what stages are RDDs are materialized and finds a minimal schedule for running the jobs.

******************************************************************************
19. What is the common workflow of a spark program?
The most common workflow of  spark program is:

The first step is to create input RDDs depending on the external data. 
Data can be obtained from different data sources.
Post RDD creation, the RDD transformation operations like filter() or map() are run for creating new RDDs depending on the business logic.
If any intermediate RDDs are required to be reused for later purposes, we can persist those RDDs.
Lastly, if any action operations like first(), count() etc are present then spark launches it to initiate parallel computation.
*****************************************************************************************

22. What are the profilers in PySpark?
These are useful for building predictive models. Profilers are useful for data review to ensure that it is valid and can be used for consumption. Custom profilers are supported in PySpark. When we require a custom profiler, it has to define some of the methods like:

profile: This produces a system profile of some sort.
stats: This returns collected stats of profiling.
dump: This dumps the profiles to a specified path.
add: This helps to add profile to existing accumulated profile. The profile class has to be selected at the time of SparkContext creation.
dump(id, path): This dumps a specific RDD id to the path given

***************************************************************************************
24. What are the different approaches for creating RDD in PySpark?
We have so many approaches for creating RDD in Pyspark
sparkContext.parallelize(): The parallelize() method of the SparkContext can be used for creating RDDs. 
This method loads existing collection from the driver and parallelizes it. 
This is a basic approach to create RDD and is used when we have data already present in the memory. 
This also requires the presence of all data on the Driver before creating RDD. 
####Code to create RDD using the parallelize method for the python list shown in the image above:

sparkContext.textFile(): Using this method, we can read .txt file and convert them into RDD. 
#Syntax: rdd_txt = spark.sparkContext.textFile("/path/to/textFile.txt")

sparkContext.wholeTextFiles(): This function returns PairRDD (RDD containing key-value pairs) with file path being the key and the file content is the value.
#rdd_whole_text = spark.sparkContext.wholeTextFiles("/path/to/textFile.txt")

Empty RDD with no partition using sparkContext.emptyRDD: RDD with no data is called empty RDD. We can create such RDDs having no partitions by using emptyRDD() method as shown in the code piece below:
empty_rdd = spark.sparkContext.emptyRDD 
# to create empty rdd of string type
empty_rdd_string = spark.sparkContext.emptyRDD[String]

******************************************************************************************
31. What would happen if we lose RDD partitions due to the failure of the worker node?

If any RDD partition is lost, then that partition can be recomputed using operations lineage from the original fault-tolerant dataset.

When your worker is running and RDD partition will loss then nothing will happen and no reflection will be shown on your project.

This will reflect when your work will restart, then your project will be reflected error and this not be restart again. To start it’s again you will have to solve all errors.

****************************************************************************************

Que 13. What do mean by Broadcast variables?

Ans.  Broadcast variable are read-only shared variables that are cached and available on all nodes of the cluster, In order to save the copy of data across all nodes, we use it. 
With SparkContext.broadcast(), a broadcast variable is created. 

***********************************************************************

Que 14. What are Accumulator variables?
Ans. In order to aggregate the information through associative and commutative operations, we use Accumulator Variables. 
They can be used to implement counters (as in MapReduce) or sums
dont read syntax
Code:  #class pyspark.Accumulator(add, value, accum_param)

*********************************************************************************
**********************************************************************************************
spark-case-when-otherwise

Like SQL "case when" statement and "S-with", statments and  "if then else" statement from popular programming languages, 
Spark SQL Dataframe also supports a kind of similar syntax using “when otherwise” or we can also use “case when” statement. 
##So let’s see an example on how to check for multiple conditions and replicate SQL CASE statement.

1. Using “when otherwise” on Spark DataFrame.
when is a Spark function, so to use it first we should import using import org.apache.spark.sql.functions.
#when before. Above code snippet replaces the value of gender with new derived value. when value not qualified with the condition, 
#we are assigning “Unknown” as value.

val df2 = df.withColumn("new_gender", when(col("gender") === "M","Male")
      .when(col("gender") === "F","Female")
      .otherwise("Unknown"))

2. Using “case when” on Spark DataFrame.

Similar to SQL syntax, we could use “case when” with expression expr() .

3. Using && and || operator
We can also use and (&&) or (||) within when function. To explain this I will use a new set of data to make it simple.

*********************************************************************************************

Reading Parquet file into DataFrame

We can always read the parquet file to a dataframe in Spark and see the content. They are of column formats and are more suitable for analytical environments,write once and read many. Parquet files are more suitable for Read intensive applications.

Spark DataFrameReader provides parquet() function (spark.read.parquet) to read the parquet files and creates a Spark DataFrame. 

##In this example, we are reading data from an apache parquet.

syntax for that is,
val df = spark.read.parquet("src/main/resources/zipcodes.parquet")  #path of the file 

**********************************************************************************************

Spark Modules:
we have 5 modules in spark, like
Spark Core
Spark SQL
Spark Streaming
Spark MLlib
Spark GraphX
*****************************************************************
Spark Dataframe – Show Full Column Contents?

PySpark Show Full Contents of a DataFrame

The only way to show the full column content we can use show() function. 
show():   It will show the Dataframe. 


#In Spark or PySpark by default truncate column content if it is longer than 20 chars when you try to output using show() method of DataFrame,
 
in order to show the full contents without truncating we need to provide false to show(false) method. 

1.2 PySpark (Spark with Python):

# Show full contents of DataFrame (PySpark)
df.show(truncate=False)

# Show top 5 rows and full column contents (PySpark)
df.show(5,truncate=False) 

# Shows top 5 rows and only 10 characters of each column (PySpark)
df.show(5,truncate=10) 

# Shows rows vertically (one line per column value) (PySpark)
df.show(vertical=True)


2. PySpark Show Full Contents of a DataFrame:
(Let’s assume) you have a similar DataFrame (mentioned above), for PySpark the syntax is slightly different to show the full contents of the columns. Here you need to specify truncate=False to show() method.
df.show(truncate=False)

*********************************************************************************

RDD Operations:

On Spark RDD, you can perform two kinds of operations.
RDD Transformations and RDD Actions

RDD Transformations:
Spark RDD Transformations are lazy operations meaning they don’t execute until you call an action on RDD. Since RDD’s are immutable, When you run a transformation(for example map()), instead of updating a current RDD, it returns a new RDD.

Some of the transformations on RDD’s are flatMap(), map(), reduceByKey(), filter(), sortByKey() and all these return a new RDD instead of updating the current RDD.

RDD Actions:
RDD Action operation returns the values from an RDD to a driver node. In other words, any RDD function that returns non RDD[T] is considered as an action. RDD operations trigger the computation and return RDD in a List to the driver program.

Some actions on RDD’s are count(),  collect(),  first(),  max(),  reduce()  and more.

***************************************************************************************
How to create an empty DataFrame?
While working with files, some times we may not receive a file for processing, however, we still need to create a DataFrame similar to the DataFrame we create when we receive a file. If we don’t create with the same schema, our operations/transformations on DF fail as we refer to the columns that may not present.

To handle situations similar to these, we always need to create a DataFrame with the same schema, which means the same column names and datatypes regardless of the file exists or empty file processing

Creating an empty DataFrame (Spark 2.x and above):
SparkSession provides an emptyDataFrame() method, which returns the empty DataFrame with empty schema, but we wanted to create with the specified StructType schema.

Syntax for that is:
df = spark.emptyDataFrame

Create empty DataFrame with schema (StructType)
Use createDataFrame() from SparkSession

df = spark.createDataFrame(spark.sparkContext
      .emptyRDD[Row], schema)
**********************************************************************************************
Spark DataFrame Select First Row of Each Group?

2. Select First Row From a Group
We can select the first row from the group using Spark SQL or DataFrame API, #we will see with DataFrame API using a window function row_rumber and partitionBy.

simpleData = Seq(("James","Sales",3000),
      ("Michael","Sales",4600),
      ("Robert","Sales",4100),
      ("Maria","Finance",3000),
      ("Raman","Finance",3000),
      ("Scott","Finance",3300),
      ("Jen","Finance",3900),
      ("Jeff","Marketing",3000),
      ("Kumar","Marketing",2000)
    )
import spark.implicits._
val df = simpleData.toDF("Name","Department","Salary")
df.show()

w2 = Window.partitionBy("department").orderBy(col("salary"))
    df.withColumn("row",row_number.over(w2))
      .where($"row" === 1).drop("row")
      .show()

On above snippet, first, we are partitioning on department column which groups all same departments into a group and then apply order on salary column. Now, And will use this window with row_number function. This snippet outputs the following.

row_number function returns a sequential number starting from 1 within a window partition group.

3. Retrieve Employee who earns the highest salary
To retrieve the highest salary for each department, will use orderby “salary” in descending order and retrieve the first element.
w3 = Window.partitionBy("department").orderBy(col("salary").desc)
    df.withColumn("row",row_number.over(w3))
      .where($"row" === 1).drop("row")
      .show()

4. Select the Highest, Lowest, Average, and Total salary for each department group

Here, we will retrieve the Highest, Average, Total and Lowest salary for each group. Below snippet uses partitionBy and row_number along with aggregation functions avg, sum, min, and max.
w4 = Window.partitionBy("department")
    val aggDF = df.withColumn("row",row_number.over(w3))
      .withColumn("avg", avg(col("salary")).over(w4))
      .withColumn("sum", sum(col("salary")).over(w4))
      .withColumn("min", min(col("salary")).over(w4))
      .withColumn("max", max(col("salary")).over(w4))
      .where(col("row")===1).select("department","avg","sum","min","max")
      .show()
*********************************************************************************************

Spark Repartition() vs Coalesce():

DataFrame coalesce()
Spark DataFrame coalesce() is used only to decrease the number of partitions. This is an optimized or improved version of repartition() where the movement of the data across the partitions is fewer using coalesce.
Syntax for that is:
df3 = df.coalesce()  #3
 println(df3.rdd.partitions.length)


DataFrame repartition()
Similar to RDD, the Spark DataFrame repartition() method is used to increase or decrease the partitions. ##The below example increases the partitions 

###from 5 to 6 by moving data from all partitions.
Syntax for that is:
df2 = df.repartition()  #6
println(df2.rdd.partitions.length)

**********************************************************************************
Spark SQL Join on multiple columns:

Using Join syntax:
#join(right: Dataset[_], joinExprs: Column, joinType: String): DataFram
This join syntax takes, takes right dataset, joinExprs and joinType as arguments and we use joinExprs to provide join condition on multiple columns.

//Using multiple columns on join expression
  empDF.join(deptDF, empDF("dept_id") === deptDF("dept_id") &&
    empDF("branch_id") === deptDF("branch_id"),"inner")
      .show(false)


Using Where to provide Join condition
Instead of using a join condition with join() operator, we can use where() to provide a join condition.
//Using Join with multiple columns on where clause 
  empDF.join(deptDF).where(empDF("dept_id") === deptDF("dept_id") &&
    empDF("branch_id") === deptDF("branch_id"))
    .show(false)

Using Filter to provide Join condition
We can also use filter() to provide Spark Join condition, below example we have provided join with multiple column
//Using Join with multiple columns on filter clause
  empDF.join(deptDF).filter(empDF("dept_id") === deptDF("dept_id") &&
    empDF("branch_id") === deptDF("branch_id"))
    .show(false)



****************************************************************************************
Spark Window Functions

spark window function operate on a group of row and return the single value for every input
spark support 3 kinds of windows funtions:

ranking functions
analytic functions
aggregate functions
################
ranking functions:
RANK() will assign non-consecutive “ranks” to the values
ranking functions are of 3 types: 
    row_number window function
    rank window function 
    dense_rank window function 

row_number Window Function: row_number() window function is used to give the sequential row number starting from 1 to the result of each window partition.

windowSpec  = Window.partitionBy("department").orderBy("salary")
df.withColumn("row_number",row_number.over(windowSpec))
  .show()

rank Window Function: rank() window function is used to provide a rank to the result within a window partition. This function leaves gaps in rank when there are ties.
df.withColumn("rank",rank().over(windowSpec))
  .show()

2.3 dense_rank Window Function
dense_rank() window function is used to get the result with rank of rows within a window partition without any gaps. This is similar to rank() function difference being rank function leaves gaps in rank when there are ties.
df.withColumn("dense_rank",dense_rank().over(windowSpec))
  .show()
#######################################################
analytic functions:
analytic functions are of 2 types:
    lag window function 
    lead window function

 lag Window Function: This is the same as the LAG function in SQL.
lead Window Function: This is the same as the LEAD function in SQL.
########################################################################
df.read
Aggregate Functions:

using this function calculate sum, min, max for each department using Spark SQL Aggregate window functions and WindowSpec. 
When working with Aggregate functions, we don’t need to use order by clause.


val windowSpecAgg  = Window.partitionBy("department")

val aggDF = df.withColumn("row",row_number.over(windowSpec))
    .withColumn("avg", avg(col("salary")).over(windowSpecAgg))
    .withColumn("sum", sum(col("salary")).over(windowSpecAgg))
    .withColumn("min", min(col("salary")).over(windowSpecAgg))
    .withColumn("max", max(col("salary")).over(windowSpecAgg))
    .where(col("row")==1).select("department","avg","sum","min","max")
    .show()
    

*****************************************************************************

Link for Window functions:
https://sparkbyexamples.com/spark/spark-sql-window-functions/#ranking-functions


***********************************************************************************
Spark SQL map Functions:
Spark SQL map functions are grouped as “collection_funcs” in spark SQL along with several array functions. These map functions are useful when we want to concatenate two or more map columns, convert arrays of StructType entries to map column 
Few of the sql map functions are
map	        Creates a new map column.
map_keys	Returns an array containing the keys of the map.
map_values	Returns an array containing the values of the map.
map_concat	Merges maps specified in arguments.
map_from_entries	Returns a map from the given array of StructType entries.
map_entries	Returns an array of all StructType in the given map.
explode(e: Column)	Creates a new row for every key-value pair in the map by ignoring null & empty. It creates two new columns one for key and one for value.
explode_outer(e: Column)	Creates a new row for every key-value pair in the map including null & empty. It creates two new columns one for key and one for value.
posexplode(e: Column)	Creates a new row for each key-value pair in a map by ignoring null & empty. It also creates 3 columns “pos” to hold the position of the map element, “key” and “value” columns for every row.
posexplode_outer(e: Column)	Creates a new row for each key-value pair in a map including null & empty. It also creates 3 columns “pos” to hold the position of the map element, “key” and “value” columns for every row.
transform_keys(expr: Column, f: (Column, Column) => Column)	Transforms map by applying functions to every key-value pair and returns a transformed map.
transform_values(expr: Column, f: (Column, Column) => Column)	Transforms map by applying functions to every key-value pair and returns a transformed map.
map_zip_with( left: Column, right: Column, f: (Column, Column, Column) => Column)	Merges two maps into a single map.
element_at(column: Column, value: Any)	Returns a value of a key in a map.
size(e: Column)	Returns length of a map column.

https://sparkbyexamples.com/spark/spark-sql-map-functions/

******************************************************************************************
LINK:

https://sparkbyexamples.com/

Spark String Functions
Spark Sort Functions
Spark Date and Time Functions
How to convert Parquet file to CSV file
How to process JSON from a CSV file
How to convert Parquet file to CSV file



It is nice taking to you, Thanks for your time.
