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
                 sh 'cd demo_testing_pipeline'
                 sh 'cd apitest'
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
