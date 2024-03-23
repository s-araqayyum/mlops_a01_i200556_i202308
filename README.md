# MLOps CI/CD Pipeline Documentation

## Overview 🌐

This document outlines the Continuous Integration/Continuous Deployment (CI/CD) pipeline designed for our project, which includes a machine learning model and a unique dataset for each group. Our pipeline integrates several tools and technologies, including Jenkins, GitHub, Docker, Python, and Flask, to automate testing, building, and deployment processes.

## Team Members 👥

- Member 1: Sara Qayyum, s-araqayyum
- Member 2: Fouzan Yaseen, fozanyaseen

## Pipeline Workflow 🔄

### 1. Development Workflow 🛠️

**Branches:**

- `main`: Stable version of the project.
- `dev`: Development branch where all features are pushed till successful feature completion.
- `test`: Branch for running automated tests.

**Code Quality Checks:** On pushing changes to the `dev` branch, a GitHub Actions workflow is triggered to perform code quality checks using flake8.

### 2. Pull Requests and Code Review ✅

- **Admin Approval:** Changes pushed to `dev` require a pull request and approval from a group admin before merging, ensuring code review and quality, the same is required for all other branches.

### 3. Automated Testing 🧪

- On merging changes to the `test` branch, another GitHub Actions workflow triggers automated unit tests to verify the application's functionality.

### 4. Deployment 🚀

- **Dockerization and Push to Docker Hub:** Successful completion of tests on the `test` branch, and a subsequent merger to main after a pull request triggers a Jenkins job that dockerizes the application and pushes the Docker image to Docker Hub.
- **Post-Merge to Main:** Upon merging, a notification is sent to the administrator (i202308@nu.edu.pk), indicating the successful execution of the Jenkins job.

## Tools and Technologies 🛠️

- **Jenkins:** Automates the Dockerization process and pushes the Docker image to Docker Hub.
- **GitHub Actions:** Manages automated code quality checks and unit testing.
- **Docker:** Containerizes the application for consistent deployment.
- **Python & Flask:** Backend technology stack for application development.

## Setup and Configuration ⚙️

### Jenkins

- Jenkins is configured to monitor the `main` branch for changes. It uses a webhook to trigger the Dockerization process.
- The `Jenkinsfile` includes steps for building the Docker image and pushing it to Docker Hub.

### GitHub Actions

- Two workflows are defined:
  - `.github/workflows/code_quality.yml` for flake8 checks on the `dev` branch.
  - `.github/workflows/autotester.yml` for running automated tests on the `test` branch.

### Docker

- A `Dockerfile` is included at the root of the repository, specifying the build instructions for the application image.

### Notifications 📧

- Email notifications are set up in Jenkins to alert the administrator upon the successful deployment of the application to Docker Hub.

## Conclusion 🎯

This CI/CD pipeline streamlines our development process, ensuring that our application is thoroughly tested and reliably deployed with minimal manual intervention.
