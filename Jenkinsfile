pipeline {
    agent any

    environment {
        IMAGE_NAME = 'wizards-almanac'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master',
                    url: 'http://git.codesubmit.io/frontline-data-solutions/devops-1-sknbrb',
                    credentialsId: 'codesubmit-git'
            }
        }

        stage('Read Version') {
            steps {
                script {
                    env.APP_VERSION = readFile('app/VERSION').trim()
                    echo "Building version: ${env.APP_VERSION}"
                }
            }
        }

        stage('Build Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${env.APP_VERSION} ./app"
            }
        }

        stage('Deploy') {
            steps {
                sh "APP_VERSION=${env.APP_VERSION} docker-compose up -d"
            }
        }
    }
}