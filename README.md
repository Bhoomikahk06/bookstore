1. Testing Strategy

In our unit testing approach, we concentrate on verifying key API functionalities, particularly login and CRUD operations. The signup and login processes are organized in conftest.py, with signup executed once per session to generate a Bearer token for test execution.

	•	 Each test includes assertions to confirm expected outcomes, such as correct status codes and the structure of response data.

	•	 We utilize logging to document significant events and outcomes, facilitating issue diagnosis when tests fail and helping to identify root causes quickly.

	•	 Tests are included for expected failure scenarios, like accessing a non-existent book, ensuring the API handles errors gracefully.

	•	 Each test is clearly named to enhance readability and clarity.

	•	 By using @pytest.mark.run(order=x), we can control the order of test execution, which is essential when certain tests depend on the results of others.

	•	 Each test is designed to manage expected failures gracefully, providing detailed log messages for context during troubleshooting.

3. CI/CD Setup with Jenkins

	Follow these steps to set up Jenkins for Continuous Integration and Continuous Deployment (CI/CD):
	1.	Download Jenkins:
		Go to the Jenkins download page and download the Windows installer (.msi file).
	2.	Install Jenkins:
		Double-click the downloaded .msi file and follow the installation prompts, selecting default options.
	3.	Access Jenkins:
		Open your web browser and navigate to http://localhost:8080.
	4.	Unlock Jenkins:
		On the initial setup page, you’ll need an unlock key found at C:\Program Files (x86)\Jenkins\secrets\initialAdminPassword. Copy and paste this key to unlock Jenkins.
	5.	Create Admin User:
  		Follow the prompts to create your first admin user.
	6.	Log In:
		Sign in using the credentials you just created.
	7.	Manage Jenkins:
		Click on "Manage Jenkins" from the dashboard.
	8.	Create a Pipeline Project:
		Select "New Item" and choose "Pipeline." Configure the pipeline using the Groovy script from your Git repository.
	9.	Build the Project:
		After configuration is complete, click "Build Now" to trigger the pipeline.

3.To Run Locally

•	Clone the code from the Repository :
    https://github.com/Bhoomikahk06/bookstore.git
    
•	Navigate to the project directory:
    cd bookstore
    
•	Install the required packages:
    pip install -r requirements.txt
    
•	Running the Application Start the FastAPI server
    uvicorn main:app –reload
    
•	Open New Terminal and Run all the tests using below command
    pytest -v -s  --html=demo.html --capture=tee-sys      

