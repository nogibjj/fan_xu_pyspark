from pyspark.sql import SparkSession
from script import load_data, explore_data, process_data, transformation


def save_to_markdown(filename, content):
    """
    Save the given content to a markdown file.
    """
    with open(filename, "w") as f:
        f.write(content)


def main():
    # Initialize Spark session
    spark = SparkSession.builder.appName("NBAplayers").getOrCreate()

    # Initialize content for markdown
    markdown_content = "# NBA Stats Analysis\n\n"

    # Load data from local file
    df = load_data(spark)
    markdown_content += "## Data Loading\n\nData loaded successfully.\n\n"
    # Explore data
    exploration_output = explore_data(df)
    markdown_content += "## Data Exploration\n\n"
    markdown_content += (
        "### First 3 Rows\n\n" + exploration_output["first_rows"] + "\n\n"
    )
    markdown_content += (
        f"### Total Number of Observations/Rows: {exploration_output['row_count']}\n\n"
    )
    markdown_content += (
        "### Summary Statistics\n\n" + exploration_output["summary_stats"] + "\n\n"
    )

    # Process data (register as SQL table and do SQL Queries)
    process_output = process_data(spark, df)
    markdown_content += "## SQL Queries\n\n"
    markdown_content += (
        "### Top 10 Highest Scoring Players\n\n" + process_output["query"] + "\n\n"
    )

    # Transformation 1
    winner_output = transformation(df)
    markdown_content += "## Data Transformation\n\n"
    markdown_content += (
        "### Creating a column to calculate Assist/Turnover Ratio (1st 10 rows)\n\n"
        + winner_output
        + "\n\n"
    )

    # Stop the Spark session
    spark.stop()

    # Save all outputs to a markdown file
    save_to_markdown("output.md", markdown_content)


if __name__ == "__main__":
    main()
