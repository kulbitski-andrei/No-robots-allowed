# No-robots-allowed

## About

Final project on Python Test Automation course. 
Contain UI and API tests for website https://thinking-tester-contact-list.herokuapp.com/.
Made by Andrei Kulbitski, Ekaterina Tsiunel and Yanislav Terentev in 2024.

## Project Structure

```plaintext
/No-robots-allowed
├── .github
│   ├── workflows
├── log_test
│   ├── log_setup.py
├── pages
├── test_data
├── tests
│   ├── api
│   │   ├── contacts
│   │   ├── user
│   ├── ui
├── .gitignore
├── .pylintrc
├── Dockerfile
├── pytest.ini
├── README.md
└── requirements.txt
```

## Usage

### Requirements
- Python >=3.8
- pip
- Docker

### How to install
Clone the repository:
```bash
git clone <URL>
```
Create a Virtual environment:
```bash
cd ~/projects/No-robots-allowed
python -m venv No-robots-allowed
. venv/bin/activate
```
Install dependencies
```bash
pip install -r requirements.txt
```

### How to run tests
To execute ALL tests with DEBUG log level
```bash
pytest . --log-level=DEBUG
```
To execute ALL API test cases
```bash
pytest . -m API
```
To execute ALL UI test cases
```bash
pytest . -m UI
```

### Available markers:
```
high: Run high priority tests.
medium: Run medium priority tests.
regress: Run regress test suite
smoke: Run smoke test suite.
API: Run api test suite.
UI: Run ui test suite.
```

## Running Tests with Docker and Jenkins

### Docker setup
* dockerfile is in the repository
- Navigate to your project directory
```bash
docker build --platform linux/amd64 .
docker run -d -p 8080:8080 -p 50000:50000 --restart=on-failure <imageID>  
```

Access to Jenkins: http://localhost:8080

### Configure Jenkins Pipeline
* jenkinsfile is in the repository
- Create a new Jenkins pipeline
- Set up the pipeline script to execute the pytest command


### Run Tests Automatically:
It is possible to run tests automatically on code commits or schedule them to run at specific intervals.
