pipeline {
agent any
    stages {

        stage('login') {
            steps {
                sh 'aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 562278399407.dkr.ecr.us-east-1.amazonaws.com'
            }
        }

        stage('build') {
            steps {
                sh 'docker build -t forkube-jenkins .'
            }
        }

      stage('tag') {
            steps {
                sh 'docker tag forkube-jenkins:latest 562278399407.dkr.ecr.us-east-1.amazonaws.com/forkube-jenkins:latest'
            }
        }

         stage('push') {
            steps {
                sh 'docker push 562278399407.dkr.ecr.us-east-1.amazonaws.com/forkube-jenkins:latest'
            }
        } 
       stage('deploy') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
            }
        }   
    } 

    }