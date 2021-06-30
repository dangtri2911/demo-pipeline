pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                 sh '''#!/bin/bash
                 echo "hello world"
                 echo "update here"
                 '''
            }
        }
        
        stage('test') {
            steps {
                 sh '''#!/bin/bash
                 echo "testing..."
                 '''
            }
        }

        stage('deploy') {
            steps {
                 sh '''#!/bin/bash
                 echo "deploying..."
                 '''
            }
        }
    }
    
}
