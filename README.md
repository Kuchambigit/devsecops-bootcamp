DevSecOps Hands-on & Interview Bootcamp
Project Overview

This repository documents my hands-on DevSecOps learning journey, using a personal Proxmox homelab to build, secure, deploy, and monitor applications.

The objective is to strengthen my understanding of DevOps and DevSecOps technologies while preparing for technical interviews.
Lab Environment

    Hypervisor: Proxmox VE

    Operating System: Ubuntu 26.04 LTS

    Virtual Machine: VM 103

    CPU: 4 vCPUs

    RAM: 3.3 GiB

    Storage: 99 GB root filesystem

    Architecture: x86_64

Learning Roadmap
Phase	Topic	Status
1	Linux Fundamentals	In Progress
2	Git and GitHub	In Progress
3	Docker and Docker Compose	Planned
4	Jenkins CI/CD	Planned
5	Ansible Automation	Planned
6	Kubernetes	Planned
7	Helm	Planned
8	DevSecOps Security Tools	Planned
9	Monitoring and Observability	Planned
10	Terraform and Infrastructure as Code	Planned
DevSecOps Security Tools

The security phase will cover:

    Gitleaks — Secret scanning

    SonarQube — Static application security testing

    OWASP Dependency-Check — Dependency vulnerability scanning

    Trivy — Container image scanning

    OWASP ZAP — Dynamic application security testing

Documentation Standards

Each lab will include:

    Learning objectives

    Technical explanations

    Commands and configurations

    Screenshots and verification results

    Troubleshooting notes

    Interview questions and answers

Current Progress
Lab 1 — Linux Environment Assessment

Completed:

    Identified operating system and kernel.

    Examined CPU, memory, and disk resources.

    Checked existing DevOps tools.

    Verified Docker service functionality.

    Initialized a local Git repository.

See 01-linux-fundamentals/system-inventory.md for detailed findings.
Goal

Develop practical DevSecOps engineering skills through repeatable hands-on labs, security automation, CI/CD implementation, Kubernetes deployments, and continuous monitoring.

## Module 04: Docker Security Remediation

### Objective
Identify and remediate security vulnerabilities in a Dockerized NGINX application using SonarQube Cloud and Docker security best practices.

### 1. Security Finding

**Tool:** SonarQube Cloud  
**File:** `04-docker-automation/webapp/Dockerfile`  
**Finding:** NGINX container runs as the root user by default.  
**Severity:** Low

**Security Risk:** Running containers as root increases the potential impact of a container compromise.

### 2. Security Remediation

Replaced the original NGINX base image with an unprivileged version.

**Original image:**
`nginx:alpine`

**Secured image:**
`nginxinc/nginx-unprivileged:stable-alpine`

Additional changes:
- Removed the package upgrade command that required elevated permissions.
- Changed the exposed container port from 80 to 8080.
- Retained the custom HTML application.

### 3. Docker Image Build

Built the secured image using:

```bash
# Build the secured NGINX Docker image
docker build -t devsecops-webapp:secure ./04-docker-automation/webapp
```

**Result:** Docker image built successfully.

### 4. Verify Non-Root Execution

```bash
# Check the user identity inside the secured container
docker run --rm devsecops-webapp:secure id
```

**Verification output:**

```text
uid=101(nginx) gid=101(nginx) groups=101(nginx),101(nginx)
```

**Result:** Confirmed that NGINX runs as a non-root user.

### 5. Application Functionality Testing

The existing application was using port 8080, while Jenkins was using port 8081.

To avoid disrupting existing services, the secured container was deployed using host port 8082.

```bash
# Start the secured application on host port 8082
docker run -d \
  --name devsecops-secure-webapp \
  -p 8082:8080 \
  devsecops-webapp:secure

# Verify the secured application responds
curl http://localhost:8082
```

**Result:** The application successfully returned the DevSecOps Bootcamp HTML page.

### 6. SonarQube Security Verification

After committing and pushing the remediation to GitHub, SonarQube Cloud completed another analysis.

**Results:**
- Open issues: 0
- Top-priority issues: 0
- Dockerfile security finding: Resolved

### 7. Key Lessons Learned

- Containers should run with the minimum privileges necessary.
- Docker base images influence the security of containerized applications.
- Security changes should be validated through functional testing.
- Port conflicts can be resolved without interrupting existing services.
- Automated static analysis helps identify and track security weaknesses.

### Final Outcome

**Module 04 Docker Security Remediation: Completed Successfully.**

The application now runs using an unprivileged NGINX image, and its functionality has been verified.
