# CS/EC528-Project

## 1. Vision and Goals Of The Project:

Self Service Cloud-Native Data Analysis Platform is a platform for data scientists to ingest and analyze data on the cloud based on user specific requirements.

Goals:
- Providing a platform for modern ETL (Extract/Transform/Load) pipeline  
- Develop a data science infrastructure within the cloud that can:  
                - Pull data from a bucket and return it to that   
                - Transform the data  
                - Leverage standardized data science software (tensorflow, BigQuery etc.)  
- Present decisions made throughout the development process along with tradeoffs between the current approach and available alternatives  


** **

## 2. Users/Personas Of The Project:
The platform will be used by data scientists from companies and government institutions.
- A user who needs to run machine learning models in Tensorflow/Pytorch to predict stock trends based on previous stock data stored in a remote GCS bucket  
- A user who wants to preprocess their data using numeric python and load to a remote S3 bucket.
- A user who needs to use sql to query and search a specific item in data stored in a remote S3 bucket  


It doesn’t target:
- End-users who need to deal with extremely large datasets
- End-users who follow standard pipeline and don’t need customized solution
- Institutions with unique use cases considering the development of their own service


** **

## 3.   Scope and Features Of The Project:

- Self-service allocation based on the description of the detailed pipeline component needs.
- Leverages standardized software to analyse data.
- Provides storage for user data which is able to pull data from one or multiple source
- Provides ability to run python codes to transform and analyze data
- Provides support for sql commands to query the database
- Security: only select users are able to access and modify the data.
- Ability for multiple users to use simultaneously and independently


** **

## 4. Solution Concept
High-level outline of the solution:
- Storage for Data: cloud-native technologies like AWS S3/GCP GCS/ DynamoDB/Spanner
- Computing Engine: use existing IaaS solutions like AWS EC2 or GCP (can also use Container solution) 
- Data Analysis: use data analysis platforms like Jupyter and Pandas to support machine learning codes of Tensorflow/Pytorch. (We could start simple with sklearn just to test our pipeline)
- Permission and Access Control: Provide security solutions between services and external access (Cloud IAM)
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
Release #1 (due by Week 5):
Data extraction and storage  
When end-users decide to upload the data, we can extract the data from their buckets and store them in our built databases.

Release #2 (due by Week 9):
Data transformation

Release #3 (due by Week 11):
Incorporation of standardized data science software.

Release #4 (due by Week 13):
Security and access

Release #5 (due by Week 15):
Final Product and report

** **
## Team
- Ibrahim Chand
- Zihang Jiang
- Anish Yennapusa
- Ze Yu

## Mentors
- Dan Hyland: dan.hyland@twosigma.com
- Edward Yang: edward.yang@twosigma.com
