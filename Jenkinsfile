pipeline {
    agent any

    environment {
        SPLUNK_HOME = "C:\\Program Files\\Splunk"      // your Splunk install path
        REPO_CONF_DIR = "C:\\splunk-config-repo"        // local clone path for generated confs
        SPLUNK_BIN = "\"C:\\Program Files\\Splunk\\bin\\splunk.exe\""
    }

    stages {
        stage('Checkout Repository') {
            steps {
                checkout scm
            }
        }

        stage('Generate Splunk Config Files') {
            steps {
                bat 'python scripts\\generate_configs.py'   // update path if needed
            }
        }

        stage('Deploy Configs to Local Splunk') {
            steps {
                bat '''
                echo Copying configs...
                xcopy /Y /E "%WORKSPACE%\\generated_confs\\*" "%SPLUNK_HOME%\\etc\\system\\local\\"
                '''
            }
        }

        stage('Restart Splunk') {
            steps {
                bat '''
                echo Restarting Splunk...
                %SPLUNK_BIN% restart
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Splunk configuration deployed and restarted successfully.'
        }
        failure {
            echo '❌ Deployment failed. Check logs.'
        }
    }
}
