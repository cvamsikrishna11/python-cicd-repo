# Python CI/CD Repository

This repository demonstrates a Python project with a CI/CD pipeline using Jenkins. The pipeline includes creating a virtual environment, installing dependencies, running tests with coverage, and generating test and coverage reports.

## Final output screenshot

![Jenkins Pipeline Results](https://github.com/cvamsikrishna11/python-cicd-repo/blob/main/result.png)


![Code Coverage Summary](https://github.com/cvamsikrishna11/python-cicd-repo/blob/main/coverage-summary.png)


## Prerequisites

1. Jenkins installed on your system or server. (You can utilize this EC2 userdata to setup the jenkins and python https://github.com/cvamsikrishna11/devops-fully-automated/blob/installations/jenkins-maven-ansible-setup.sh)
2. Python 3.x installed on your Jenkins build agent.

## Required Jenkins Plugins

1. Cobertura Plugin
2. JUnit Plugin
3. Code Coverage API Plugin

### Installing Jenkins Plugins

To install the required plugins, follow these steps:

1. Go to your Jenkins dashboard and click on "Manage Jenkins" in the left sidebar.
2. Click on "Manage Plugins."
3. In the "Available" tab, search for "Cobertura", "Code Coverage API Plugin" and "JUnit."
4. Check the boxes next to "Cobertura Plugin", "Code Coverage API Plugin"  and "JUnit Plugin," then click "Install without restart" or "Download now and install after restart."

## Setting Up the Build Process

1. Clone this repository to your local machine.
2. In Jenkins, create a new Pipeline job.
3. In the Pipeline job configuration, select "Pipeline script from SCM" under the "Pipeline" section.
4. Choose "Git" as the SCM and enter the URL of your repository (https://github.com/cvamsikrishna11/python-cicd-repo.git).
5. Save the job configuration.

## Running the Build Process

1. Click "Build Now" in your Jenkins Pipeline job to start the build process.
2. Monitor the build progress in the "Console Output" of the running build.
3. Once the build is completed, you can view the test and coverage reports in the "Test Result" and "Cobertura Coverage Report" sections of the build page.

## Further Assistance

For additional help or questions, please open an issue in the repository or reach out to the repository owner.
