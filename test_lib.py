"""file for testing lib.py"""

import pytest
from pyspark.sql import SparkSession
from script import load_data, explore_data, transformation


@pytest.fixture(scope="module")
def spark():
    """Fixture to initialize a SparkSession."""
    return SparkSession.builder.appName("NBAplayers").getOrCreate()


@pytest.fixture(scope="module")
def sample_data(spark):
    """Fixture to create a sample DataFrame for testing."""
    data = [
        ("1", "John", 24, "Chicago", "C", 20, 3, 0, 1),
        ("2", "Bob", 25, "Houston", "PF", 25, 4, 1, 3),
        ("3", "Frank", 30, "Dallas", "PG", 10, 5, 2, 2),
    ]
    columns = ["Rk", "Player", "Age", "Team", "Pos", "PTS", "AST", "STL", "TOV"]
    return spark.createDataFrame(data, schema=columns)


def test_load_data(spark):
    """Test the load_data function."""
    df = load_data(spark, local_path="NBA_24_stats.csv")
    assert df is not None
    assert len(df.columns) > 0


def test_explore_data(sample_data):
    """Test the explore_data function."""
    output = explore_data(sample_data)
    assert "first_rows" in output
    assert "row_count" in output
    assert output["row_count"] == 3  # Check sample data row count
    assert "summary_stats" in output


def test_transformation(sample_data):
    """Test the declare_winner function."""
    output = transformation(sample_data)
    assert output is not None
