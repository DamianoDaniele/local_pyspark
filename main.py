import os
import sys
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Imposta PYSPARK_PYTHON con l'interprete corrente
os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["HADOOP_HOME"] = "C:\\Users\\Utente\\hadoop"
os.environ["hadoop.home.dir"] = "C:\\Users\\Utente\\hadoop"
print("Versione Python:", sys.version)


spark = (SparkSession.builder
         .appName("test_local_oyspark")
         .getOrCreate())

data = [
    ("James", "", "Smith", "36636", "M", 3000),
    ("Michael", "Rose", "", "40288", "M", 4000),
    ("Robert", "", "Williams", "42114", "M", 4000),
    ("Maria", "Anne", "Jones", "39192", "F", 4000),
]

schema = StructType([
    StructField("firstname", StringType(), True),
    StructField("middlename", StringType(), True),
    StructField("lastname", StringType(), True),
    StructField("id", StringType(), True),
    StructField("gender", StringType(), True),
    StructField("salary", IntegerType(), True)
])

df = spark.createDataFrame(data, schema)
df.printSchema()
print(df.count())
first = df.head()
print(first)
df.show()




