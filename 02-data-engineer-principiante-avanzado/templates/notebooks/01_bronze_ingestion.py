# Databricks source notebook template
# Candidate: implement the ingestion and persistence logic.

from pyspark.sql import functions as F

INPUT_PATH = "<configure-input-path>"
BRONZE_PATH = "<configure-bronze-path>"

# TODO: define explicit schemas and read customers, projects, work_logs and incidents.
# TODO: add ingestion_timestamp and source_file.
# TODO: persist Bronze data in Delta format.