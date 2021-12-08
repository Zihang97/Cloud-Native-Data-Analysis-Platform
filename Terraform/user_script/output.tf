output "SSH_via_UNIX_User" {
  value = "ssh ${var.username}@${aws_instance.hub_instance.public_dns}"
}

resource "local_file" "output" {
  content = aws_instance.hub_instance.public_dns
  filename = "output.txt"
}