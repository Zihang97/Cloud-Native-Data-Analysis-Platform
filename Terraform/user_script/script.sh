#!/bin/bash
sleep 1m
# Log stdout to file
# exec redirects the shell output to where you specifiy
# The numbers are file descriptors - 0=stdin 1=stdout 2=stderr
# Create a new FD 3 and redirect it to stdout
# Create a new FD 4 and redirect it to stderr
exec 3>&1 4>&2
trap 'exec 2>&4 1>&3' 0 1 2 3
exec 1>/home/user/terraform.log 2>&1
# Create Unix User
sudo useradd -s /bin/bash -m -d /home/user -g root user
echo "user:password1" | chpasswd
echo 'user ALL=(ALL:ALL) ALL' | sudo EDITOR='tee -a' visudo
sudo sed -i '61s/.*/PasswordAuthentication yes/' /etc/ssh/sshd_config
sudo sed -i '63s/.*/#PasswordAuthentication no/' /etc/ssh/sshd_config
sudo systemctl restart sshd.service
# Update AL2
sudo yum update -y
# Mount /anaconda3
sudo mkfs.xfs /dev/sdb -f
sudo mkdir /anaconda3
sudo mount /dev/sdb /anaconda3
sudo chown -R user:user /anaconda3
sudo echo "UUID=$(lsblk -nr -o UUID,MOUNTPOINT | grep "/anaconda3" | cut -d ' ' -f 1) /anaconda3 xfs defaults,nofail 1 2" >> /etc/fstab
# Install Anaconda
wget https://repo.anaconda.com/archive/Anaconda3-2018.12-Linux-x86_64.sh -O /home/user/anaconda.sh &&
    bash /home/user/anaconda.sh -u -b -p /anaconda3 &&
    echo 'export PATH="/anaconda3/bin:$PATH"' >> /home/user/.bashrc &&
    rm -rf /home/user/anaconda.sh &&
# Configure Jupyter for AWS HTTP
runuser -l user -c 'jupyter notebook --generate-config' &&
    sed -i -e "s/#c.NotebookApp.ip = 'localhost'/c.NotebookApp.ip = '"$(curl http://169.254.169.254/latest/meta-data/public-hostname)"'/g" /home/user/.jupyter/jupyter_notebook_config.py &&
    sed -i -e "s/#c.NotebookApp.allow_origin = ''/c.NotebookApp.allow_origin = '*'/g" /home/user/.jupyter/jupyter_notebook_config.py &&
    sed -i -e "s/#c.NotebookApp.open_browser = True/c.NotebookApp.open_browser = False/g" /home/user/.jupyter/jupyter_notebook_config.py
# Reference: https://github.com/wblakecannon/terraform-jupyter