pipeline {
    agent any  // Use any available agent
 
    environment {
        // Set environment variables if needed
        GITHUB_REPO = 'https://github.com/Bhoomikahk06/bookstore.git'
        BRANCH_NAME = 'main'
    }
 
    stages {
        stage('Checkout') {
            steps {
                script {
                    // Checkout the code from GitHub
                    git url: "${GITHUB_REPO}", branch: "${BRANCH_NAME}"
                }
            }
        }
 
        stage('Install Requirements') {
            steps {
                script {
                    echo 'Installing Requirements...'
                    bat 'cd ./bookstore && pip install -r requirements.txt --quiet'  
                }
            }
        }

		stage("Parallel Steps"){
			parallel{
				stage('Run FastAPI') {
					steps {
						script {
							echo 'Running FastAPI...'
							bat 'cd ./bookstore && start /B cmd /c "uvicorn main:app --reload"'
                            echo "Started Uvicorn Server"
						}
					}
				}
				stage('Run Tests') {
					steps {
						script {
							echo 'Running tests...'
							bat 'cd ./bookstore/tests &&  pytest -v -s  test_demo.py --html=demo.html --capture=tee-sys'
						}
					}
				}
			}
		}
    }
 
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
        always {
            script {
                echo 'Stopping Uvicorn...'
                bat 'taskkill /F /IM uvicorn.exe'
            }
        }
    }
}