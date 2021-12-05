variable "availability_zone" {
    default = "us-east-2a"
}

variable "instance_type" {
    default = "t2.micro"
}

variable "service" {
    default = "hub_instance"
}

variable "central_bucket_name" {
    default = "common-repo-cloud"
}

variable "customer_bucket_name" {
    default = "user4-cloud"
}

variable "username" {
    default = "user"
}

variable "tag_name" {
    default = "Name"
}

variable "tag_value" {
    default = "EC2_Intance_Name"
}