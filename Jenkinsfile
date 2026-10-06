pipeline {
    agent any

    stages {

        stage('Environment Check') {
            steps {
                sh 'python3 --version'
                sh 'git --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install -r requirements.txt'
            }
        }
    }
}
