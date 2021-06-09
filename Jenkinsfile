pipeline {
  /* environment {
    registry = "680696743786.dkr.ecr.eu-central-1.amazonaws.com/mkokocha-kupse"
    registryCredential = ‘my.aws.credentials’
  } */
  agent any
  stages {
    stage('Cloning Git') {
      steps {
        git 'https://github.com/pisarz/kupse_online.git'
      }
    }
    stage('Building image') {
      steps{
        docker build -t kupse-jenkins:${BUILD_NUMBER} .
        docker tag kupse-jenkins:${BUILD_NUMBER} jenkins-demo:latest  
        }
      }
    }
    /* stage('Push image') {
      steps{
        script {
          docker.withRegistry(
              'https://680696743786.dkr.ecr.eu-central-1.amazonaws.com'
              'ecr:eu-central-1:AKIAZ47FQA5VOLBEHUHD') {
                  def myImage = docker.build('mkokocha-kupse')
                  myImage.push('jenkins')
              }
        }
      }
    } */
  }
}
