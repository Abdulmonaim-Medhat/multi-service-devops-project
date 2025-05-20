# Multi-Service DevOps Pipeline  
## Architecture  
![Diagram](docs/architecture.png)  

## CI/CD Pipeline  
- **Stages**: Build → Test → Deploy  
- **Tools**: GitLab CI, Docker, AWS EC2  

## Setup  
```bash
# Local testing
docker-compose up -d

# Infrastructure (Terraform)
cd infra && terraform apply
