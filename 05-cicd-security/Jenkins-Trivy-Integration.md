# Jenkins CI/CD Pipeline with Trivy Security Scanning

## 1. Project Overview

This milestone demonstrates how to integrate automated container vulnerability scanning into a Jenkins CI/CD pipeline.

The objective is to identify HIGH and CRITICAL vulnerabilities in Docker images and prevent vulnerable images from passing the pipeline's security validation stage.

### Technologies Used

- Jenkins — CI/CD automation
- Docker — Container image building
- Trivy — Container vulnerability scanning
- Git and GitHub — Source code management
- Ubuntu Linux — Jenkins host
- NGINX Alpine — Containerized web application

## 2. Project Architecture

The implemented pipeline follows this workflow:

**GitHub → Jenkins → Docker Build → Trivy Security Scan → Build Success/Failure**

The pipeline contains four stages:

1. **Checkout:** Retrieve source code from GitHub.
2. **Environment Check:** Verify required tools and build environment.
3. **Docker Build:** Build a fresh Docker image.
4. **Security Validation:** Scan the image for HIGH and CRITICAL vulnerabilities.

The pipeline fails when Trivy detects vulnerabilities at the configured severity levels.

## 3. Initial Security Findings

An initial Trivy scan identified vulnerabilities in the NGINX Alpine Docker image.

**Image:** `devsecops-webapp:v2`

**Scan results:**

| Severity | Vulnerabilities |
|---|---:|
| HIGH | 3 |
| CRITICAL | 0 |
| Total | 3 |

### Vulnerabilities Identified

| CVE | Package | Severity |
|---|---|---|
| CVE-2026-125350 | libxslt | HIGH |
| CVE-2026-87636 | libxslt | HIGH |
| CVE-2026-9947 | libxslt | HIGH |

The installed `libxslt` version was `1.1.43-r3`.

Trivy identified `1.1.43-r4` as the fixed version.

## 4. Vulnerability Remediation

The Dockerfile was updated to install available Alpine security patches during the image build.

### Updated Dockerfile

```dockerfile
# Use the official NGINX Alpine base image
FROM nginx:alpine

# Install available Alpine package security updates
RUN apk upgrade --no-cache

# Copy the application webpage into the container
COPY index.html /usr/share/nginx/html/index.html

# Document the HTTP port used by NGINX
EXPOSE 80
```

The package updates included:

- `libxslt`: `1.1.43-r3` → `1.1.43-r4`
- `zlib`: `1.3.2-r1` → `1.4-r0`

### Rebuild the Docker Image

```bash
# Build the patched Docker image
docker build --pull -t devsecops-webapp:v3 .
```

### Verify the Security Fix

```bash
# Scan the patched image for HIGH and CRITICAL vulnerabilities
trivy image --scanners vuln --severity HIGH,CRITICAL devsecops-webapp:v3
```

**Result:** Zero HIGH or CRITICAL vulnerabilities were detected.

## 5. Jenkins Pipeline Integration

The Jenkins pipeline is defined in:

`05-cicd-security/Jenkinsfile`

### Docker Build Stage

```groovy
// Build the application image from the repository Dockerfile
stage('Docker Build') {
    steps {
        sh 'docker build --pull -t devsecops-webapp:ci ./04-docker-automation/webapp'
    }
}
```

### Security Validation Stage

```groovy
// Scan the freshly built image and fail on HIGH or CRITICAL findings
stage('Security Validation') {
    steps {
        sh 'trivy image --severity HIGH,CRITICAL --exit-code 1 --scanners vuln devsecops-webapp:ci'
    }
}
```

The `--exit-code 1` option causes the security validation stage to fail when matching vulnerabilities are detected.

This establishes an automated security gate in the CI/CD pipeline.

## 6. Jenkins Build Results

**Jenkins Job:** `devsecops-security-pipeline`

**Successful Build:** `#4`

**Docker Image:** `devsecops-webapp:ci`

### Final Results

| Validation | Result |
|---|---|
| GitHub Checkout | Passed |
| Environment Check | Passed |
| Docker Image Build | Passed |
| Trivy Security Validation | Passed |
| HIGH Vulnerabilities | 0 |
| CRITICAL Vulnerabilities | 0 |
| Jenkins Build Status | SUCCESS |

Jenkins console output confirmed:

`SUCCESS: Docker image built and passed Trivy security scanning.`

`Finished: SUCCESS`

## 7. Security Benefits

This integration demonstrates several DevSecOps practices:

- **Shift-left security:** Detect vulnerabilities during CI rather than after deployment.
- **Automated security gates:** Fail builds that exceed the configured vulnerability threshold.
- **Container hardening:** Apply available package security updates.
- **Continuous validation:** Scan newly built container images.
- **Version control:** Track security changes through GitHub.

**Scope:** This scan validates HIGH and CRITICAL vulnerabilities reported by Trivy. It does not establish that the image is free of all vulnerabilities or security risks.

## 8. Evidence and Screenshots

Add the following screenshots to the repository documentation:

1. Initial Trivy scan showing three HIGH vulnerabilities.
2. Updated Dockerfile containing the Alpine package upgrade.
3. Successful Trivy scan showing zero HIGH and CRITICAL vulnerabilities.
4. Jenkins Build #4 console output showing `Finished: SUCCESS`.

## 9. Interview-Ready Explanation

I implemented automated Docker image vulnerability scanning within a Jenkins CI/CD pipeline using Trivy.

Initially, Trivy detected three HIGH-severity vulnerabilities associated with the `libxslt` package in our NGINX Alpine container image.

I investigated the findings, identified available security patches, and updated the Dockerfile to apply package upgrades during the image build.

I then integrated Trivy into Jenkins as a security validation stage, configuring the pipeline to fail automatically when HIGH or CRITICAL vulnerabilities are detected.

After committing the Dockerfile changes to GitHub and rebuilding the image through Jenkins, the pipeline completed successfully with zero HIGH or CRITICAL vulnerabilities reported.

This implementation demonstrates automated security validation, vulnerability remediation, and shift-left security practices within a CI/CD workflow.

## 10. Conclusion

The Jenkins and Trivy integration was completed successfully.

The pipeline now builds the application image, performs automated vulnerability scanning, and enforces a security gate before reporting success.

**Final Status: SUCCESS — Jenkins Build #4**
