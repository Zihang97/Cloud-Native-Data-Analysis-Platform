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
    default = "ec528-central-bucket-terraform"
}

variable "customer_bucket_name" {
    default = "ec528-customer-bucket-terraform"
}
