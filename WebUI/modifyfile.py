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
		content[9] = f'exec 1>/home/{username}/terraform.log 2>&1'
		content[16] = f'sudo chown -R {username}:{username} /anaconda3'
		content[19] = f'sudo useradd -s /bin/bash -m -d /home/{username} -g root {username}'
		content[20] = f'echo "{username}:password1" | chpasswd'
		content[21] = f"echo '{username} ALL=(ALL:ALL) ALL' | sudo EDITOR='tee -a' visudo"
		content[26] = f'wget https://repo.anaconda.com/archive/Anaconda3-2018.12-Linux-x86_64.sh -O /home/{username}/anaconda.sh &&'
		content[27] = f'    bash /home/{username}/anaconda.sh -u -b -p /anaconda3 &&'
		content[28] = f'    echo \'export PATH="/anaconda3/bin:$PATH"\' >> /home/{username}/.bashrc &&'
		content[29] = f'    rm -rf /home/{username}/anaconda.sh &&'
		content[31] = f'runuser -l {username} -c \'jupyter notebook --generate-config\' &&'
		content[32] = f'    sed -i -e "s/#c.NotebookApp.ip = \'localhost\'/c.NotebookApp.ip = \'"$(curl http://169.254.169.254/latest/meta-data/public-hostname)"\'/g" /home/{username}/.jupyter/jupyter_notebook_config.py &&'
		content[33] = f'    sed -i -e "s/#c.NotebookApp.allow_origin = \'\'/c.NotebookApp.allow_origin = \'*\'/g" /home/{username}/.jupyter/jupyter_notebook_config.py &&'
		content[34] = f'    sed -i -e "s/#c.NotebookApp.open_browser = True/c.NotebookApp.open_browser = False/g" /home/{username}/.jupyter/jupyter_notebook_config.py'
		for line in content:
			print(line, file = f)

def read_dns():
	content = []
	with open("./output.txt", "r") as f:
		for line in f:
			content.append(line)
	return content[0]

# modify_var("ec528-jzh-cloud", "jzh", "jzh_pipeline1")
modify_script("user")
# print(read_dns())