output "SSH via Key" {
  value = "ssh -i ${aws_key_pair.generated_key.key_name}.pem ec2-user@${aws_instance.central_instance.public_dns}"
}

output "SSH via UNIX User" {
  value = "ssh ${var.username}@${aws_instance.central_instance.public_dns}"
}

resource "local_file" "output" {
  content = aws_instance.central_instance.public_dns
  filename = "output.txt"
}