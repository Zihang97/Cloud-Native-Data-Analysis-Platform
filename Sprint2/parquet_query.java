package com.sparkbyexamples.spark.dataframe

object CsvToParquet extends App {

  val spark: SparkSession = SparkSession.builder()
    .master("local[1]")
    .appName("SparkByExample")
    .getOrCreate()

  spark.sparkContext.setLogLevel("ERROR")

  //read csv with options
  val df = spark.read.options(Map("inferSchema"->"true","delimiter"->",","header"->"true"))
    .csv("../../project/ridership.csv")
  df.show()
  df.printSchema()

  //convert to parquet
  df.write.parquet("../../project/ridership.parquet")
}

object ParquetQuery extends App {

  val spark: SparkSession = SparkSession.builder()
    .master("local[1]")
    .appName("SparkByExample")
    .getOrCreate()

  spark.sparkContext.setLogLevel("ERROR")

  val sqlContext = new org.apache.spark.sql.SQLContext(sc)

  val parqfile = sqlContext.read.parquet(“ridership.parquet”)

  parqfile.registerTempTable(“ridership”)

  spark.time(spark.sql("select * from ridership;").show())
}


