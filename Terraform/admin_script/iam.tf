resource "aws_iam_role" "admin_role" {
    name = "user_role"
    assume_role_policy = jsonencode({
        Version = "2012-10-17"
        Statement = [{
            Action = "sts:AssumeRole"
            Effect = "Allow"
            Sid = ""
            Principal = {
                Service = "ec2.amazonaws.com"
            }
        }]
    })
}

resource "aws_iam_role_policy" "admin_role_policy" {
    name = "admin_role_policy"
    role = "${aws_iam_role.admin_role.id}" 
    policy = jsonencode({
        Version = "2012-10-17"
        Statement = [
            {
                Effect = "Allow",
                Action = "*",
                Resource = "*"
            }
        ]
    })
}

resource "aws_iam_instance_profile" "instance_profile" {
    name = "instance_profile"
    role = "${aws_iam_role.admin_role.name}"
}
