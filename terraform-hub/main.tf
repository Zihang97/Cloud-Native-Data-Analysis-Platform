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

resource "tls_private_key" "key" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "aws_key_pair" "generated_key" {
  key_name   = "key-${uuid()}"
  public_key = "${tls_private_key.key.public_key_openssh}"
}

resource "local_file" "pem" {
  filename        = "${aws_key_pair.generated_key.key_name}.pem"
  content         = "${tls_private_key.key.private_key_pem}"
  file_permission = "400"
}

resource "aws_security_group" "hub_instance" {
  name        = "${var.service}-${uuid()}"
  description = "Security group for ${title(var.service)}"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "SSH"
  }

  ingress {
    from_port   = 8888
    to_port     = 8898
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "${title(var.service)}"
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "hub_instance" {
  ami                    = "${data.aws_ami.al2.id}"
  availability_zone      = "${var.availability_zone}"
  instance_type          = "${var.instance_type}"
  key_name               = "${aws_key_pair.generated_key.key_name}"
  iam_instance_profile = "${aws_iam_instance_profile.instance_profile.name}"
  vpc_security_group_ids = ["${aws_security_group.hub_instance.id}"]
  user_data              = "${file("script.sh")}"
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

resource "aws_s3_bucket" "central_bucket" {
  bucket = "${var.central_bucket_name}"
  acl    = "private"
}

resource "aws_s3_bucket" "customer_bucket" {
  bucket = "${var.customer_bucket_name}"
  acl    = "private"
}

terraform {
  backend "local" {
  }
}
