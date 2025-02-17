# AWS Data Pipeline with S3, Glue, and Athena

## **Project Overview**
This project sets up a data pipeline on AWS using **S3, AWS Glue, and Athena** to process and analyze raw COVID-19 data.

The pipeline follows these steps:
1. **Store raw data** in an S3 bucket.
2. **Use AWS Glue** to crawl and catalog the data.
3. **Query the data using Athena**.

## **Technologies Used**
- **Amazon S3**: Cloud storage for raw and processed data.
- **AWS Glue**: Managed ETL service to catalog and transform data.
- **Amazon Athena**: Interactive SQL queries for analyzing data in S3.

---

## **Project Setup: Step-by-Step Guide**

### **1. Create and Upload Data to S3**
1. Sign in to [AWS Console](https://aws.amazon.com/console/).
2. Navigate to **S3**.
3. Click **Create bucket**.
   - Bucket name: `covid19-data-pipeline-af-south-1`
   - Region: `af-south-1`
   - Disable block public access.
   - Click **Create bucket**.
4. Upload your **CSV file**:
   - Click on the created bucket.
   - Click **Upload** → **Add files** → Select your CSV file.
   - Click **Upload**.

### **2. Configure AWS Glue Crawler**
1. Navigate to **AWS Glue Console**.
2. Click **Crawlers** → **Create crawler**.
3. Enter **Crawler name**: `covid19-data-crawler`.
4. Click **Next** → Choose **S3** as the data source.
5. Enter S3 path: `s3://covid19-data-pipeline-af-south-1/`
6. Click **Next** → Choose **IAM Role**: `AWSGlueServiceRole`.
7. Click **Next** → **Create and Run the Crawler**.
8. Wait until status changes to **Succeeded**.

### **3. Query Data in Athena**
1. Navigate to **Amazon Athena**.
2. Go to **Settings**.
3. Set query result location to:
