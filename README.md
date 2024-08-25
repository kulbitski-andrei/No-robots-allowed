# No-robots-allowed

About

Final project on Python Test Automation course. 
Contain UI and API tests for website https://thinking-tester-contact-list.herokuapp.com/.
Made by Andrei Kulbitski, Ekaterina Tsiunel and Yanislav Terentev in 2024.

Project structure

/pytest-framework
├── .github
│   ├── workflows
│   │   ├── flake8.yaml
│   │   ├── ...
├── pages
│   │   ├── base.py
│   │   ├── ...
│   ├── calculator.py
├── test_data
│   ├── constants.py
│   ├── service_methods.py
├── tests
│   ├── api
│   │   ├──contacts
│   │   │   ├── conftest.py
│   │   │   ├── test_
│   │   │   ├── ...
│   │   ├──users
│   │   │   ├── conftest.py
│   │   │   ├── test_
│   │   │   ├── ...
│   │   ├──data_api_users.py
│   │   ├──Jenkinsfile
│   ├── ui
│   │   ├── conftest.py
│   │   ├── Jenkinsfile
│   │   ├── test_add_contacts.py
│   │   ├── ...
├── .gitignore
├── .pylintrc
├── Dockerfile 
├── pytest.ini
├── README.md
└── requirements.txt