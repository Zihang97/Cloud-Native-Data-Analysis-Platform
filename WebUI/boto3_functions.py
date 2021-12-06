import boto3
from botocore.exceptions import ClientError

def find_instance_id(tag_name):
	ec2 = boto3.client('ec2', region_name='us-east-2')
	custom_filter = [{
	    'Name':'tag:Name', 
	    'Values': [tag_name]}]
	response = ec2.describe_instances(Filters=custom_filter)
	instance_id = response['Reservations'][0]["Instances"][0]["InstanceId"]
	return instance_id

def startec2(instance_id):
	ec2 = boto3.client('ec2', region_name='us-east-2')
	try:
		ec2.start_instances(InstanceIds=[instance_id], DryRun=True)
	except ClientError as e:
		if 'DryRunOperation' not in str(e):
			raise

    # Dry run succeeded, run start_instances without dryrun
	try:
		response = ec2.start_instances(InstanceIds=[instance_id], DryRun=False)
	except ClientError as e:
		print(e)


def stopec2(instance_id):
	ec2 = boto3.client('ec2', region_name='us-east-2')
	try:
		ec2.stop_instances(InstanceIds=[instance_id], DryRun=True)
	except ClientError as e:
		if 'DryRunOperation' not in str(e):
			raise

	# Dry run succeeded, call stop_instances without dryrun
	try:
		response = ec2.stop_instances(InstanceIds=[instance_id], DryRun=False)
	except ClientError as e:
		print(e)


def terminateec2(instance_id):
	ec2 = boto3.client('ec2', region_name='us-east-2')
	try:
		ec2.terminate_instances(InstanceIds=[instance_id], DryRun=True)
	except ClientError as e:
		if 'DryRunOperation' not in str(e):
			raise

	# Dry run succeeded, call terminate_instances without dryrun
	try:
		response = ec2.terminate_instances(InstanceIds=[instance_id], DryRun=False)
	except ClientError as e:
		print(e)

# instance_id = find_instance_id('jzhpipeline7')
# startec2(instance_id)