pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/haripriyakamaraj2410/midterm.git'
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'token',
                                                 usernameVariable: 'DOCKER_USER',
                                                 passwordVariable: 'DOCKER_PASS')]) {
                    bat '''
                        docker logout
                        echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin
                    '''
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -f dockerfile -t haripriyakamaraj2410/app:latest .'
            }
        }

        stage('Push Docker Image') {
            steps {
                bat 'docker push haripriyakamaraj2410/app:latest'
            }
        }

        stage('Run Container') {
            steps {
                bat '''
                    docker stop midterm-app || echo "No old container"
                    docker rm midterm-app || echo "No container to remove"
                    echo "5" | docker run --rm --name midterm-app haripriyakamaraj2410/app:latest
                '''
            }
        }
    }

    post {
        always {
            bat 'docker logout'
        }
        success {
            echo '✅ Pipeline completed successfully!'
        }
    }
}
