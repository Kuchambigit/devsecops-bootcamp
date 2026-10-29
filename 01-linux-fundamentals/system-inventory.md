
# DevSecOps Bootcamp — Lab 1

## Objective
Assess the existing Ubuntu environment before installing
DevSecOps tools.

## Environment

- Hypervisor: Proxmox VE
- Virtual Machine: VM 103
- Hostname: Katud-ubuntu-edtechserver
- Operating System: Ubuntu 26.04 LTS
- Kernel: 7.0.0-38-generic
- Architecture: x86_64
- Virtual CPUs: 4
- Total RAM: 3.3 GiB
- Available RAM: Approximately 900 MiB
- Root Disk: 99 GB
- Available Disk: 77 GB

## Installed Tools

| Tool | Version | Status |
|------|---------|--------|
| Git | 2.53.0 | Installed |
| Python | 3.14.4 | Installed |
| Docker | 29.1.3 | Running |
| Docker Compose | 2.40.3 | Installed |
| Terraform | 1.15.8 | Installed |
| Ansible | Not detected | Pending installation check |
| Jenkins | Not detected | Service inactive |
| Kubernetes (K3s) | Not detected | Service inactive |
| Helm | Not detected | Pending installation check |
| Trivy | Not detected | Pending installation check |

## Commands Used

- `whoami` — Identify the current user.
- `hostname` — Identify the server.
- `cat /etc/os-release` — Identify the operating system.
- `lscpu` — Display CPU information.
- `free -h` — Display memory usage.
- `df -h` — Display filesystem disk usage.
- `uname -r` — Display kernel version.
- `git --version` — Check Git version.
- `python3 --version` — Check Python version.
- `docker --version` — Check Docker version.
- `docker compose version` — Check Docker Compose.
- `ansible --version` — Check Ansible.
- `helm version --short` — Check Helm.
- `terraform version` — Check Terraform.
- `trivy --version` — Check Trivy.
- `docker ps` — List running Docker containers.
- `systemctl is-active docker` — Check Docker service.
- `systemctl is-active jenkins` — Check Jenkins service.
- `systemctl is-active k3s` — Check K3s service.

## Findings

1. Docker is installed and operational.
2. No Docker containers are currently running.
3. Jenkins and K3s services are inactive.
4. Available RAM is limited.
5. Disk capacity is sufficient for initial labs.
6. Existing EdTech project files will be preserved.

## Next Steps

1. Complete installed software inventory.
2. Check existing Docker images and containers.
3. Configure GitHub repository.
4. Begin Linux fundamentals training.
