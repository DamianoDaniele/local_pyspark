import os
import sys
import pytest
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType


# Fixture per creare una sessione Spark condivisa per i test
@pytest.fixture(scope="session")
def spark():
    os.environ["PYSPARK_PYTHON"] = sys.executable
    os.environ["HADOOP_HOME"] = "C:\\Users\\Utente\\hadoop"
    os.environ["hadoop.home.dir"] = "C:\\Users\\Utente\\hadoop"

    spark_instance = (
        SparkSession.builder
        .appName("pytest-pyspark-local-testing")
        .getOrCreate()
    )
    yield spark_instance


def test_create_dataframe(spark):
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

    # Verifica che il DataFrame abbia esattamente 4 righe
    print(f"Questa è la prima riga: {df.head()} \n")
    print(f"Questa è la prima riga: {df.first()} \n")
    assert df.count() == 4

    # Verifica che lo schema contenga i nomi di colonna attesi
    expected_columns = ["firstname", "middlename", "lastname", "id", "gender", "salary"]
    assert df.columns == expected_columns
