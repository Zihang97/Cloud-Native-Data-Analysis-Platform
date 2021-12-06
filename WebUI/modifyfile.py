def modify_var(bucket_name, username, instance_name):
	content = []
	with open("./terraform/var.tf", "r") as f:
		for line in f:
			line = line[:-1]
			content.append(line)

	with open("./terraform/var.tf", "w") as f:
		content[17] = f'    default = "{bucket_name}"'
		content[21] = f'    default = "{username}"'
		content[29] = f'    default = "{instance_name}"'
		for line in content:
			print(line, file = f)


def modify_script(username):
	content = []
	with open("./terraform/script.sh", "r") as f:
		for line in f:
			line = line[:-1]
			content.append(line)

	with open("./terraform/script.sh", "w") as f:
		content[19] = f'sudo useradd -s /bin/bash -m -d /home/{username} -g root {username}'
		content[20] = f'echo "{username}:password1" | chpasswd'
		content[21] = f"echo '{username} ALL=(ALL:ALL) ALL' | sudo EDITOR='tee -a' visudo"
		for line in content:
			print(line, file = f)

def read_dns():
	content = []
	with open("./output.txt", "r") as f:
		for line in f:
			content.append(line)
	return content[0]

# modify_var("ec528-jzh-cloud", "jzh", "jzh_pipeline1")
# modify_script("jzh")
# print(read_dns())