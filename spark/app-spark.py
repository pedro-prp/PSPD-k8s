from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("WordcountSparkK8s").getOrCreate()


def process_request(text):
    rdd = spark.sparkContext.parallelize([text])
    return rdd.flatMap(lambda x: x.split()).count()


if __name__ == "__main__":
    print(process_request("Hello Spark on Kubernetes"))
