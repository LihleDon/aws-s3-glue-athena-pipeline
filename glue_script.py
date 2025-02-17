import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# Initialize Glue job
args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Read data from S3
datasource0 = glueContext.create_dynamic_frame.from_options(
    format_options={},
    connection_type="s3",
    format="csv",
    connection_options={"paths": ["s3://covid19-data-pipeline-af-south-1/raw/"], "recurse": True},
    transformation_ctx="datasource0"
)

# Write transformed data to processed folder
glueContext.write_dynamic_frame.from_options(
    frame=datasource0,
    connection_type="s3",
    connection_options={"path": "s3://covid19-data-pipeline-af-south-1/processed/"},
    format="parquet"
)

job.commit()
