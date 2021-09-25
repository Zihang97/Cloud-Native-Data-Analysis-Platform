# CS/EC528-Project

## 1. Vision and Goals Of The Project:

Self Service Cloud-Native Data Analysis Platform (referred as “Piggy Platform” from now on) is a platform for arbitrary end-users to manipulate and analyze cloud data quickly and efficiently.

Goals:
- Providing a platform for a modern ETL (Extract/Transform/Load)
- Provide users with flexible options for data analysis with several data science platforms (Jupyter/Pandas/etc)
- Implement permission and access controls for end-users to ensure data security and independence
- Present decisions made throughout the development process along with tradeoffs between the current approach and available alternatives

## 2. Users/Personas Of The Project:
Piggy Platform will be used by data scientists from companies and government institutions.

It doesn’t target:
- End-users who need to deal with extremely large datasets
- End-users who follow standard pipeline and don’t need customized solution
- Institutions with unique use cases considering the development of their own service


** **

## 3.   Scope and Features Of The Project:

Piggy Platform
- Presents a self service portal for end-users
  - Select compute type (RAM/CPU/GPU/etc)
  - Select data science platform to use (Jupyter, pandas, etc)
  - Add/Change/Delete pipelines
- Provides a front-end UI for end-users to interface with
- Provides storage solution for user data
- Provides tools to transform and analyze data
- Ability for multiple users to use simultaneously and independently
- Security: user data are secure and independent
- Permission/Access: only allowed users can access Piggy Platform
- Scalability: can scale to large number of users

** **

## 4. Solution Concept
High-level outline of the solution:
- Storage for Data: cloud-native technologies like AWS S3/GCP GCS/ DynamoDB/Spanner
- Computing Engine: use existing IaaS solutions like AWS EC2 or GCP (can also use Container solution) 
- Data Analysis: use data analysis platforms like Jupyter and Pandas to support machine learning codes of Tensorflow/Pytorch. (We could start simple with sklearn just to test our pipeline)
- Permission and Access Control: Provide security solutions between services and external access
- Front-end UI: HTML/CSS/JS for webpage and  Python Flask for web application

## 5. Acceptance criteria
Minimum acceptance criteria is a self service portal with a user friendly UI that can help end-users operate pipeline and analyze data. 
Stretch goals include:
- Use this project to analyze Boston Open Data
- Provide several compute and size options

## 6.  Release Planning:
Release #1 (due by Week 5):
Data extraction and storage
When end-users decide to upload the data, we can extract the data from their buckets and store them in our built databases.

Release #2 (due by Week 9):
Data transformation & analysis

Release #3 (due by Week 11):
User Interface

Release #4 (due by Week 13):
Security and access

Release #4 (due by Week 15):
Final Product

## Mentor
Dan Hyland:
dan.hyland@twosigma.com

Edward Yang:
edward.yang@twosigma.com

Professor Orran Krieger:
okrieg@bu.edu

Professor Peter Desnoyers:
pjd-nu or pjd@ccs.neu.edu

Anqi Guo:
anqianqi1
