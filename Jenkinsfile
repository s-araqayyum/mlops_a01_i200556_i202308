pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                bat "docker login --username saraqayyum --password maleeha1234"
                // Build the Docker image
                bat "docker build -t saraqayyum/emotion-detector:latest ."
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                // Push the image to Docker Hub
                bat "docker push saraqayyum/emotion-detector:latest"
            }
        }
    }

    post {
        success {
            // Email upon successfully completing the pipeline
            mail to: 'i202308@nu.edu.pk',
                 subject: "SUCCESS: Docker image pushed to Docker Hub",
                 body: "The pipeline successfully pushed the Docker image to Docker Hub."
        }
    }
}
