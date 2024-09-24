## Overview

This repository contains the source code for **bookstore**. It includes everything you need to build and test the application.

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


## To Run Locally

**Note**: Make sure Python is installed in local machine

**Clone the code from the Repository**: git clone https://github.com/Bhoomikahk06/bookstore.git
    
**Navigate to the project directory & Install the required packages**: cd bookstore && pip install -r requirements.txt
    
**Run the FastAPI server**: uvicorn main:app –reload
    
**Open New Terminal and Run all the tests using below command**: pytest -v -s  --html=demo.html --capture=tee-sys     


## Test Strategy Approach

Our unit testing strategy emphasizes validating key API functionalities, specifically login and CRUD operations. Key components include:

**Session Management**: The signup and login processes are managed in `conftest.py`, with signup executed once per session to generate a Bearer token for test execution.

**Assertions**: Each test includes assertions to verify expected outcomes, such as correct status codes and response data structure.

**Logging**: We utilize logging to document significant events and outcomes, aiding in diagnosing issues when tests fail and identifying root causes swiftly.

**Error Handling**: Tests cover expected failure scenarios, like accessing a non-existent book, ensuring the API responds gracefully to errors.

**Readability**: Each test is clearly named to enhance clarity and readability.

**Execution Order**: We control the order of test execution using `@pytest.mark.run(order=x)`, which is crucial for tests that depend on previous results.

**Graceful Failure Management**: Each test is designed to handle expected failures gracefully, providing detailed log messages to assist in troubleshooting.

