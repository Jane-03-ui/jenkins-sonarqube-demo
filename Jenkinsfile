pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Check Raw Files') {
            steps {
                sh '''
                echo "Checking unwanted files..."

                find . -type f \\( -name "*.pdf" -o -name "*.docx" \
                -o -name "*.png" -o -name "*.jpg" \\) > raw_files.txt

                if [ -s raw_files.txt ]; then
                    echo "Raw files found!"
                    cat raw_files.txt
                    exit 1
                else
                    echo "No raw files found"
                fi
                '''
            }
        }

        stage('SonarQube Scan') {
            steps {
                script {
                    def scannerHome = tool 'SonarScanner'
                    withSonarQubeEnv('SonarQube') {
                        sh "${scannerHome}/bin/sonar-scanner"
                    }
                }
            }
        }

        stage('Build Docker Image') {
            when {
                branch 'main'
            }
            steps {
                sh 'docker build -t fastapi-demo .'
            }
        }

        stage('Stop Old Container') {
            when {
                branch 'main'
            }
            steps {
                sh 'docker rm -f fastapi-app || true'
            }
        }

        stage('Deploy Container') {
            when {
                branch 'main'
            }
            steps {
                sh 'docker run -d --name fastapi-app -p 8000:8000 fastapi-demo'
            }
        }

        stage('Deployment Status') {
            when {
                branch 'main'
            }
            steps {
                sh 'docker ps'
            }
        }
    }
}
