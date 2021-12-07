variable "availability_zone" {
    default = "us-east-2a"
}

variable "instance_type" {
    default = "t2.micro"
}

variable "service" {
    default = "central_instance"
}

variable "central_bucket_name" {
    default = "ec528-central-bucket-test"
}

variable "username" {
    default = "admin"
}

variable "tag_name" {
    default = "Name"
}

variable "tag_value" {
    default = "Central"
}