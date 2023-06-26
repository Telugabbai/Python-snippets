from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lower, regexp_replace
from pyspark.sql.functions import split, explode, size, count

# Create a SparkSession
spark = SparkSession.builder.appName("LetterCount").getOrCreate()

# Enable case sensitivity
spark.conf.set("spark.sql.caseSensitive", "true")

# Create a DataFrame with the input text
input_text = "its not who i am underneath but what i do that defines me"
df = spark.createDataFrame([(input_text,)], ['text'])

# Remove non-alphabetic characters and convert to lowercase
clean_text = df.withColumn("clean_text", lower(regexp_replace(col("text"), "[^a-z]", "")))

# Split the clean text into individual letters
letter_df = clean_text.withColumn("letters", split(col("clean_text"), ""))

# Explode the letters array into separate rows
exploded_df = letter_df.select(explode(col("letters")).alias("letter"))

# Count the occurrences of each letter
letter_counts = exploded_df.groupBy("letter").agg(count("*").alias("count")).orderBy("letter")

# Show the results
letter_counts.show()
