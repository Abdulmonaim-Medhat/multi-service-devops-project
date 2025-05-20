provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "service_a" {
  ami           = "ami-08c40ec9ead489470" # Ubuntu 22.04
  instance_type = "t2.micro"
  key_name      = "DevOpsVMKey"
  tags = {
    Name = "ServiceA"
  }
}

resource "aws_instance" "service_b" {
  ami           = "ami-08c40ec9ead489470"
  instance_type = "t2.micro"
  key_name      = "DevOpsVMKey"
  tags = {
    Name = "ServiceB"
  }
}

output "service_a_ip" {
  value = aws_instance.service_a.public_ip
}

output "service_b_ip" {
  value = aws_instance.service_b.public_ip
}