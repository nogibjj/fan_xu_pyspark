def load_data(spark, local_path="NBA_24_stats.csv"):
    """
    Load data from a local CSV file into a PySpark DataFrame, clean up column names, and remove duplicate columns.
    """
    df = spark.read.csv(local_path, header=True, inferSchema=True)
    return df


def explore_data(df):
    """
    Perform basic exploration on the DataFrame.
    """
    output = {}

    # Collect first rows
    output["first_rows"] = df.limit(3).toPandas().to_markdown(index=False)

    # Count rows
    output["row_count"] = df.count()

    # Collect summary statistics
    try:
        summary_df = df.select("Age", "AST", "STL").describe().toPandas()
        output["summary_stats"] = summary_df.to_markdown(index=False)
    except Exception as e:
        output["summary_stats"] = f"Error: {e}"

    return output


def process_data(spark, df):
    """
    Perform SQL queries on the DataFrame.
    """
    output = {}

    # Register the DataFrame as a SQL table
    df.createOrReplaceTempView("nba_players")

    # Query 1
    query1_df = spark.sql(
        """
        SELECT Player, Team, Pos, PTS
        FROM nba_players
        WHERE PTS > 25
        ORDER BY PTS DESC
        LIMIT 10
    """
    )
    output["query"] = query1_df.toPandas().to_markdown(index=False)

    return output


def transformation(df):
    """
    Add assist-turnover ratio column to the DataFrame.
    """
    df = df.withColumn("AST/TOV", df["AST"] / df["TOV"])
    ratio_df = df.select("Player", "Team", "Pos", "AST/TOV").limit(10)
    return ratio_df.toPandas().to_markdown(index=False)
