output "conn" {
  value = "ssh -i \"${aws_key_pair.generated_key.key_name}.pem\" ec2-user@${aws_instance.hub_instance.public_dns}"
}
