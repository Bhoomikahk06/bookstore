## Overview

This repository contains the source code for **bookstore**. It includes everything you need to build and deploy the application.

## Jenkins Integration

A `Jenkinsfile` is included in this repository to facilitate continuous integration and deployment using Jenkins. This file defines the build pipeline for this project, allowing you to automate your build and deployment processes.

### Jenkinsfile Location

The `Jenkinsfile` can be found in the root directory of this repository. It is configured to handle the following stages:

**Checkout**: Checkout the code from the Github.
  
**Install Requirements**: Installs the requirements from the requirements.txt file.
  
**Run FastAPI**: Running the FastAPI server for local setup
  
**Run Tests**: Run the testcases using pytest


### Using the Jenkinsfile

To use the `Jenkinsfile` with Jenkins:

**Set Up Jenkins**: Ensure you have a Jenkins instance running.

**Create a New Pipeline Job**: In Jenkins, create a new pipeline job and link it to this repository.

**Configure SCM**: Point the job to your repository's URL and specify the branch you want to build.

**Run the Job**: Trigger the job to start the build process as defined in the `Jenkinsfile`.


### To Run Locally

**Clone the code from the Repository**: git clone https://github.com/Bhoomikahk06/bookstore.git
    
**Navigate to the project directory & Install the required packages**: cd bookstore && pip install -r requirements.txt
    
**Run the FastAPI server**: uvicorn main:app –reload
    
**Open New Terminal and Run all the tests using below command**: pytest -v -s  --html=demo.html --capture=tee-sys     


## Test Strategy Approach

In our unit testing approach, we concentrate on verifying key API functionalities, particularly login and CRUD operations. The signup and login processes are organized in conftest.py, with signup executed once per session to generate a Bearer token for test execution.

	•	 Each test includes assertions to confirm expected outcomes, such as correct status codes and the structure of response data.

	•	 We utilize logging to document significant events and outcomes, facilitating issue diagnosis when tests fail and helping to identify root causes quickly.

	•	 Tests are included for expected failure scenarios, like accessing a non-existent book, ensuring the API handles errors gracefully.

	•	 Each test is clearly named to enhance readability and clarity.

	•	 By using @pytest.mark.run(order=x), we can control the order of test execution, which is essential when certain tests depend on the results of others.

	•	 Each test is designed to manage expected failures gracefully, providing detailed log messages for context during troubleshooting. 

