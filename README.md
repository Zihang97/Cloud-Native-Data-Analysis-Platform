# CS/EC528-Project

## 1. Vision and Goals Of The Project:

The Self Service Cloud-Native Data Analysis Platform is a project to explore the tradeoffs of using varying levels of managed services when building an end-to-end data analysis platform.

Goals:
- Develop infrastructure that can handle an end-to-end data analysis platform use case:
  - Pull and store data in a storage solution
  - Perform transform operations and analysis on data
  - Leverage standardized data science software (Tensorflow, BigQuery, etc.)
- Develop using tools and services for each component (Compute, Storage, Data Analysis, Security, and UI) that balance the tradeoffs of managed solutions

** **

## 2. Users/Personas Of The Project:
The platform will be used by data scientists with end-to-end data analysis use cases utilizing cloud technologies.

It doesn’t target:
- Data scientists with strict security and compliance requirements
- Data scientists with pre-defined technology requirements 

** **

## 3.   Scope and Features Of The Project:
- Programmatic infrastructure management and orchestration using Terraform
- Leverage standardized software to perform data analysis
- Provide storage solutions for user data to push/pull data from one or more sources
- Support ability to run scripts (Python) to transform and analyze data
- Support SQL commands to query database
- Security: Authorization settings to control which users can access and modify data
- Ability for multiple users to work simultaneously and independently

** **

## 4. Solution Concept
High-level outline of the solution:
- Storage for Data: cloud-native technologies like AWS S3/GCP GCS/ DynamoDB/Spanner
- Computing Engine: use existing IaaS solutions like AWS EC2 or GCP (can also use Container solution) 
- Data Analysis: use data analysis platforms like Jupyter and Pandas to support machine learning codes of Tensorflow/Pytorch. (We could start simple with sklearn just to test our pipeline)
- Permission and Access Control: Provide security solutions between services and external access (Cloud IAM).  
Strech Goals:
- Front-end UI: HTML/CSS/JS for webpage and  Python Flask for web application

** **

## 5. Acceptance criteria
Minimum acceptance criteria is a self service platform that can:  
- Extract data from a cloud storage service and return it.
- Support standardised data science software (tensorflow, BigQuery etc).
- Allocate storage and computation resources to ETL pipelnes based on user requirement.


Stretch goals include:
- Use this project to analyze Boston Open Data
- Provide several compute and size options
- Build a user friendly UI to interact with the platform

** **

## 6.  Release Planning:
Release #1 (due by Week 5) - [Demo #1](https://drive.google.com/file/d/1oXEU7WKBcbGg8-MOb6BIO_EFvi4C5_9g/view?usp=sharing):
- Data extraction and storage  
- When end-users decide to upload the data, we can extract the data from their buckets and store them in our built databases.

Release #2 (due by Week 9) - [Demo #2](https://drive.google.com/file/d/1xs2OyQpqQeajm7Ldirc7uzXbDh8Poh07/view?usp=sharing):
- Data transformation

Release #3 (due by Week 11) - [Demo #3](https://drive.google.com/file/d/1hF1LRp55zbktaoLSnjxkeOUE3OAvDfsb/view?usp=sharing):
- Incorporation of standardized data science software.

Release #4 (due by Week 13):
- Security and access

Release #5 (due by Week 15):
- Final Product and report

** **

## Mentors
- Dan Hyland: dan.hyland@twosigma.com
- Edward Yang: edward.yang@twosigma.com

## Team
- Ibrahim Chand: ichand@bu.edu
- Zihang Jiang: jzh15@bu.edu
- Anish Yennapusa: anishry@bu.edu
- Ze Yu: zey@bu.edu
