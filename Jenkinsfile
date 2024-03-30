pipeline {
    agent any

    triggers {
        githubPush() // Trigger the pipeline on GitHub push events
    }

    environment {
        DOCKERHUB_CREDENTIALS = 'DOCKERHUB_CREDS'
        IMAGE_NAME = 'fatimaj/myflaskapp'
        DOCKER_HOST = 'tcp://localhost:2375'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the repository
                checkout scm
            }
        }

        stage('Code Quality Check') {
            steps {
                // Install dependencies and run Flake8 for code quality checks
                sh 'pip install flake8'
                sh 'flake8 .'
            }
        }

        stage('Unit Tests') {
            steps {
                // Install dependencies and run unit tests
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Build Docker Image') {
            steps {
                // Build the Docker image
                script {
                    docker.withServer(DOCKER_HOST) {
                        sh 'docker build -t $IMAGE_NAME .'
                    }
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                // Log in to Docker Hub and push the Docker image
                docker.withRegistry('https://index.docker.io/v1/', DOCKERHUB_CREDENTIALS) {
                    sh 'docker push $IMAGE_NAME'
                }
            }
        }

        stage('Deploy') {
            steps {
                // Deploy the application
                sh 'docker run -p 5000:5000 $IMAGE_NAME &'
            }
        }
    }

    post {
        success {
            // Notify the administrator via email on successful build
            mail to: 'i200636@nu.edu.pk',
                 subject: "Successful Jenkins Pipeline Execution",
                 body: "The Jenkins pipeline has been executed successfully."
        }
        failure {
            // Notify the administrator via email on pipeline failure
            mail to: 'i200636@nu.edu.pk',
                 subject: "Jenkins Pipeline Execution Failed",
                 body: "There was a problem during the execution of the Jenkins pipeline."
        }
    }
}
