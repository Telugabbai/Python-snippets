import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count

# Create a SparkSession
spark = SparkSession.builder.appName("Count Letters").getOrCreate()

# Create a DataFrame from the phrase
df = spark.createDataFrame(["it's not who i am underneath but what i do that defines me"], "string").toDF("phrase")

# Count the number of each letter in the phrase
letter_counts = df.select(col("phrase").split("").alias("letter")).groupBy("letter").count()


# Count the no.of words
word_counts = df.select(col("phrase").split(" ").alias("Word")).groupBy("Word").count()

# Print the letter counts
letter_counts.show()

word_counts.show()