provider "aws" {
  region  = "us-east-2"
}

data "aws_ami" "al2" {
  most_recent = true

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-ebs"]
  }

  owners = ["amazon"]
}

resource "aws_instance" "hub_instance" {
  ami                    = "${data.aws_ami.al2.id}"
  availability_zone      = "${var.availability_zone}"
  instance_type          = "${var.instance_type}"
  key_name               = "${aws_key_pair.generated_key.key_name}"
  iam_instance_profile = "${aws_iam_instance_profile.instance_profile.name}"
  vpc_security_group_ids = ["${aws_security_group.hub_instance.id}"]
  user_data              = "${file("script.sh")}"
  provisioner "file" {
    source = "./Tool"
    destination = "~/Tool"

    connection {
      type = "ssh"
      user = var.username
      password = "password1"
      host = aws_instance.hub_instance.public_dns
    }
  }
}

resource "aws_ec2_tag" "ec2_instance_tag" {
  resource_id = aws_instance.hub_instance.id
  key = var.tag_name
  value = var.tag_value
}

resource "aws_ebs_volume" "hub_instance" {
  availability_zone = "${var.availability_zone}"
  size              = 8
  type              = "gp2"
}

resource "aws_volume_attachment" "hub_instance" {
  device_name  = "/dev/sdb"
  instance_id  = "${aws_instance.hub_instance.id}"
  volume_id    = "${aws_ebs_volume.hub_instance.id}"
  force_detach = true
}

resource "aws_s3_bucket" "customer_bucket" {
  bucket = "${var.customer_bucket_name}"
  acl    = "private"
}

terraform {
  backend "local" {
  }
}
