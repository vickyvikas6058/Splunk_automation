pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Generate Configs') {
      steps {
        bat 'python scripts\\generate_conf.py'
      }
    }

    stage('Validate Configs') {
      steps {
        bat 'python scripts\\lint_conf.py'
      }
    }

    stage('Deploy to Local Splunk') {
      steps {
        // copy files into your Splunk etc\system\local or app folder
        bat '''
        xcopy /Y generated\\*.conf "C:\\Program Files\\Splunk\\etc\\system\\local\\"
        '''
        // optional Splunk restart
        bat '"C:\\Program Files\\Splunk\\bin\\splunk.exe" restart'
      }
    }
  }

  post {
    success { echo '✅ Splunk configs deployed successfully!' }
    failure { echo '❌ Build failed. Check Jenkins logs.' }
  }
}
