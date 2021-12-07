import boto3
import botocore
import os
import logging
from botocore.exceptions import ClientError

def list_buckets():
	# Retrieve the list of existing buckets
	s3 = boto3.client('s3')
	response = s3.list_buckets()

	# Output the bucket names
	print('Existing buckets:')
	for bucket in response['Buckets']:
	    print(f'  {bucket["Name"]}')


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def download_file(bucket, object_name, file_name)
	s3.download_file(bucket, object_name, file_name)



