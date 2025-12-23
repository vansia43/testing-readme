# Meditation App Infrastructure as Code

This repository contains the complete infrastructure-as-code setup for the meditation app, including:

## Infrastructure Components

### 1. Docker Configuration
- `Dockerfile` - Multi-stage Docker build for the meditation API
- `docker-compose.yml` - Local development environment with PostgreSQL and Redis

### 2. Kubernetes Manifests
- `k8s/namespace.yaml` - Kubernetes namespace for the application
- `k8s/deployment.yaml` - Application deployment with health checks and resource limits  
- `k8s/service.yaml` - ClusterIP service for internal communication

### 3. CI/CD Pipeline
- `.github/workflows/ci-cd.yml` - Complete CI/CD pipeline with testing, building, and deployment
- `.github/workflows/security-scan.yml` - Security scanning with Snyk, Trivy, and Checkov

### 4. Terraform Infrastructure
- `terraform/main.tf` - AWS infrastructure including VPC, ALB, and security groups
- `terraform/variables.tf` - Configurable variables for different environments

### 5. Monitoring & Alerting
- `monitoring/prometheus.yml` - Prometheus configuration with multiple scrape targets
- `monitoring/alert_rules.yml` - Critical alerts for error rates, response times, and database health

### 6. Load Balancer Configuration
- `nginx/nginx.conf` - Nginx reverse proxy with SSL termination, security headers, and health checks

### 7. Database Setup
- `database/migrations/001_initial_schema.sql` - Initial PostgreSQL schema with users, meditations, and sessions tables

### 8. Logging & Observability  
- `logging/fluentd.conf` - Fluentd configuration for centralized logging to Elasticsearch

### 9. Backup & Disaster Recovery
- `scripts/backup/postgres-backup.sh` - Automated PostgreSQL backup script with S3 storage and retention

### 10. API Documentation
- `openapi.yml` - OpenAPI 3.0 specification for the meditation app REST API

## Getting Started

1. **Local Development**: Use `docker-compose up` to start the local environment
2. **Production Deployment**: Apply Terraform configurations for AWS infrastructure
3. **Kubernetes Deployment**: Apply manifests in `k8s/` directory  
4. **Monitoring**: Deploy Prometheus and Grafana using configurations in `monitoring/`
5. **Security**: Enable security scanning workflows in GitHub Actions

## Architecture

The meditation app follows a microservices architecture with:
- **API Gateway**: Nginx load balancer with SSL termination
- **Application**: Node.js REST API running in Kubernetes pods  
- **Database**: PostgreSQL with automated backups
- **Cache**: Redis for session storage
- **Monitoring**: Prometheus + Grafana stack
- **Logging**: Fluentd + Elasticsearch + Kibana (ELK stack)

## Security Features

- Container vulnerability scanning with Trivy
- Dependency scanning with Snyk  
- Infrastructure scanning with Checkov
- SSL/TLS encryption with security headers
- Database connection security
- Regular automated backups with encryption