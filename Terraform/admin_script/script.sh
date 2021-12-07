#!/bin/bash
sleep 1m
# Log stdout to file
# exec redirects the shell output to where you specifiy
# The numbers are file descriptors - 0=stdin 1=stdout 2=stderr
# Create a new FD 3 and redirect it to stdout
# Create a new FD 4 and redirect it to stderr
exec 3>&1 4>&2
trap 'exec 2>&4 1>&3' 0 1 2 3
exec 1>/home/ec2-user/terraform.log 2>&1
# Update AL2
sudo yum update -y
# Create Unix User
sudo useradd -s /bin/bash -m -d /home/admin -g root admin
echo "admin:password1" | chpasswd
echo 'admin ALL=(ALL:ALL) ALL' | sudo EDITOR='tee -a' visudo
sudo sed -i '61s/.*/PasswordAuthentication yes/' /etc/ssh/sshd_config
sudo sed -i '63s/.*/#PasswordAuthentication no/' /etc/ssh/sshd_config
sudo systemctl restart sshd.service
