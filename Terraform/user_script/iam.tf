resource "aws_iam_role" "user_role" {
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

resource "aws_iam_role_policy" "user_role_policy" {
    name = "user_role_policy"
    role = "${aws_iam_role.user_role.id}" 
    policy = jsonencode({
        Version = "2012-10-17"
        Statement = [
            {
                Effect = "Allow"
                Action = ["s3:*"]
                Resource = "arn:aws:s3:::${var.customer_bucket_name}"
            },
            {
                Effect = "Allow"
                Action = [
                    "s3:ListBucket",
                    "s3:GetObject",
                ]
                Resource = [
                    "arn:aws:s3:::${var.central_bucket_name}",
                    "arn:aws:s3:::${var.central_bucket_name}/*",
                ]
            }
        ]
    })
}

resource "aws_iam_instance_profile" "instance_profile" {
    name = "instance_profile"
    role = "${aws_iam_role.user_role.name}"
}
