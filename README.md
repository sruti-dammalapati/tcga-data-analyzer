# TCGA Data Analysis using AWS RDS and DynamoDB

## Project Overview

This project demonstrates the use of AWS services — specifically Amazon RDS and DynamoDB — to manage and analyze TCGA (The Cancer Genome Atlas) data. The primary objective is to create a proof-of-concept data processing pipeline that stores clinical data in a relational database (RDS) and biospecimen data in a NoSQL database (DynamoDB).

## Features

- AWS RDS instantiation and configuration to store structured clinical data
- AWS DynamoDB table setup using CDK to manage unstructured biospecimen information
- Data ingestion from TCGA datasets
- Querying and basic data analysis
- Simple visualization using Python libraries

## Prerequisites

- **AWS Account**: Access to AWS services with permissions set for RDS, DynamoDB and CloudFormation operations
- **Python Environment**: Python 3.8 or higher
- **CDK**: AWS Cloud Development Kit CLI

## Setup

### Environment Configuration

1. **Create `.env` File**:
   Define your environment variables required for Boto3 configuration and database credentials:

    ```plaintext
    AWS_ACCESS_KEY_ID=<your-access-key-id>
    AWS_SECRET_ACCESS_KEY=<your-secret-access-key>
    AWS_REGION=<your-region>
    DB_ADMIN_NAME=<your-rds-database-name>
    DB_ADMIN_PASSWORD=<your-rds-database-password>
    ```

2. **Install Python Libraries**:
   Use pip to install necessary packages:

    ```bash
    pip install -r requirements.txt
    ```

### AWS Services

1. **RDS**:
   Use the `infra/rds_create` script to crate an `RDS` instance using `boto3` and `app/rds_upload.py` to push data into the `RDS` instance.

2. ** DynamoDB **:
   Use the `infra/ddb_create` script to create a `DynamoDB` instance using `CDK` and `app/ddb_upload` to push data into the `DynamoDB` table.

