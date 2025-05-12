pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
        IMAGE_NAME = "yourusername/salary-predictor"
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/yourusername/salary-predictor.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}:${env.BUILD_NUMBER}")
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub') {
                        docker.image("${IMAGE_NAME}:${env.BUILD_NUMBER}").push()
                        docker.image("${IMAGE_NAME}:${env.BUILD_NUMBER}").push('latest')
                    }
                }
            }
        }
    }
    post {
        success {
            mail to: 'admin@example.com',
                 subject: "Successful Deployment: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "The Docker image ${IMAGE_NAME}:${env.BUILD_NUMBER} has been pushed to Docker Hub."
        }
    }
}