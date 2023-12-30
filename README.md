# Graduation project
The diploma project was completed as part of training at the 
TeachMeSkills school. The project is an automation of 
functionality testing on the website 21vek.by using the 
following technologies and tools:

+ Programming language: Python

+ Testing framework: Pytest

+ Automation Tool: Selenium

+ Report generation tool: Allure

+ Design Pattern: Page Object Model

+ Build system: Makefile

+ Application deployment platform: Dockerfile

# Installation and launch of the project
1. Install Python if not already installed.

2. Clone the project repository: `git clone https://github.com/gonchar-viktor/graduation_project.git`

3. Go to the project directory: `cd graduation_project`

4. Install dependencies: `pip install -r requirements.txt`

5. Run the tests: `pytest -s -v --reruns 2 -n 4`

# Generating reports
1. Install Allure if not already installed.
2. Run tests with data generation for the report: 
**for chrome browser:** `make test_chrome`, **for edge browser:** `make test_edge`
3. Generate a report: 
**for chrome browser:** `make serve_results_chrome`, **for edge browser:** `make serve_results_edge`

# Project structure
+ tests/ - directory with tests
+ pages/ - directory with Page Object classes
+ locators/ - directory with locators
+ helpers/ - directory with utility functions and classes
+ elements/ - directory with utility functions and classes for footer and header elements
+ data/ - directory with test data
+ all_api/ - directory with utility functions and classes for api tests
+ Makefile - file with commands for building the project
+ requirements.txt - file with project dependencies
+ conftest.py - file for storing fixtures
+ pytest.ini - file the Pytest configuration
+ docker-compose.yml - a file with commands to run multiple containers at the same time
+ Dockerfile - a file with commands for creating a container image

# Author
+ Name: **Gonchar Viktor** - *Automation QA Engineer(Python)*
+ Email: *vita-sc2@mail.ru*
+ Telegram: *https://t.me/gonchar_viktor* 
+ Phone: *+375(29)213-74-92*