data "aws_ami" "AL2" {
    most_rcent = true
    owners = ["amazon"]

    filter {
        name = "name"
        values = "amzn2-ami-hvm-*-x86_64-ebs"
    }
}

resource "aws_instance" "hub_instance" {
    ami = "${data.aws_ami.al2.id}"
    availability_zone = "${}"
    instance_type = "${}"
    
}
