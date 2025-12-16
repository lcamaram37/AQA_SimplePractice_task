# Prior to manipulate files from this repository consider take a look to this README.md file

Repository created to share Technical and Analytical parts of the home assessment, this repository
consists of two parts:

**Technical part**
Implementation of an automated web UI test script that is focused on the basic happy path functionality
for SimplePractice's task management system using Playwright and Pytest. 
The workflow for this part contemplates a basic login to SimplePractice using given credentials.
Data used for this part of the test is located in *data.json*. However, assuming that in any case 
credentials are a sensitive topic, these can be handled in other way but for testing purposes are located 
in mentioned file.

Automated test validates following happy path:
1. User login with valid credentials
2. Navigation to Tasks page
3. New task form creation
4. Task field population
5. Task submission and verification
6. Task's statuts modified and verification

**Analytical part**
Detailed checklist that is focused on the main user flows of the Task feature that deals with management system
to ensure a comprehensive and wide test coverage.
Manual testing techniques as exploratory testing, boundary testing, field value testing were conducted in order to  
provide different escenarios considered here as the access to Tasks feature, the creation, edit, manipulation, view
and elimination of previously created tasks.

Checklist is a coverage for:
1. Task creation - all fields, validations and restrictions
2. Task verification - search and filtering functionality
3. Task assignment - multiple assignee scenarios
4. Quick task creation - rapid task entry and manipulation
5. Task completion - status validation and timestamps
6. Task unchecking - status reversions
7. Task deletion - removal verification

**Objective**
To create an automated test that validates the login process and the task creation workflow
Develop a test checklist for task management features
Demonstrate test structure, POM implementation and test data management

**Files in repository**
* QA_TaskFlow_SP.py : main test script handling login and task creation flow
* conftest.py : pytest configuration and fixtures
* data.json : test data* (Exclusive for testing purposes)
* requirements.txt : project dependencies
* TASK_CHECKLIST.md : Analytical part of the assessment
* README.md : This file
* models > login_SP.py : SimplePractice login interpretation
*        > tasks_SP.py : SimplePractice tasks workflow

**Technology implemented**
Python 3.13.2 - Programming language
Playwright 1.57 - Web automation framework
Pytest 9.0.2 - Testing framework

**Installation**
**Pre-requisites**
- Python 3.8 or higher
- pip or pip3

**Set-up instructions**
1. Clone repository
   in terminal:
   git clone <repository-url>
   cd AQA_SimplePractice_task

2. Install dependencies
   in terminal:
   pip install -r requirements.txt
   
4. (If needed) verify Playwright browser installation
   in terminal:
   playwright install

**Configuration (security detail)**
As it was mentioned before, it may be the case that data.json file may be updated with
proper or current SimplePractice credentials

**To run the tests:**
in terminal:
pytest -v -s QA_TaskFlow_SP.py

**Result:**
Statements are print in terminal after the workflow is created and run specifying if the test Passed or Failed

**Created:**
Dec 16th 2025, 17:20pm

