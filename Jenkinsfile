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
                    // Use double quotes around variables to prevent issues with special characters
                    bat """
                        docker logout
                        echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin
                    """
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
                    docker stop midterm-app || exit 0
                    docker rm midterm-app || exit 0
                    :: The -i flag is crucial to allow the piped "5" to enter the container
                    echo 5 | docker run -i --rm --name midterm-app haripriyakamaraj2410/app:latest
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
        failure {
            echo '❌ Pipeline failed. Check the console output for errors.'
        }
    }
}
