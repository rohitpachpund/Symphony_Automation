pipeline {
    agent any

    stages {

        stage('Environment Check') {
            steps {
                sh 'python3 --version'
                sh 'git --version'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                sh 'python3 -m venv .venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '.venv/bin/python -m pip install --upgrade pip'
                sh '.venv/bin/python -m pip install -r requirements.txt'
            }
        }

        stage('Install Playwright Browser') {
            steps {
                sh '.venv/bin/python -m playwright install chromium'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'xvfb-run -a .venv/bin/python -m pytest --alluredir=allure-results'
            }
        }
    }
}