# Uses the latest stable version of Jenkins
FROM jenkins/jenkins:latest

# Root user
USER root

# Update list packages and install dependencies

RUN apt-get update && \
    apt-get install -y python3-pip python3-venv wget curl unzip gnupg


# Добавление официального ключа и репозитория Google Chrome
RUN curl -fsSL https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update

RUN apt-get update && \
    apt-get install -y wget curl unzip gnupg2 build-essential libssl-dev libreadline-dev zlib1g-dev \
    libnss3 libgdk-pixbuf2.0-0 libgtk-3-0 libx11-xcb1 libxcomposite1 libxdamage1 libxrandr2 libxtst6 \
    libxss1 libatspi2.0-0 libpangocairo-1.0-0 libpango-1.0-0 libcups2 libgbm1

## Install Google Chrome latest stable version
#ARG CHROME_VERSION="116.0.5845.140-1"
#RUN wget --no-verbose -O /tmp/chrome.deb https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_${CHROME_VERSION}_amd64.deb \
#  && apt install -y /tmp/chrome.deb \
#  && rm /tmp/chrome.deb

# Установка последней версии Google Chrome
RUN apt-get install -y google-chrome-stable


# Установка подходящей версии ChromeDriver
RUN wget -O /tmp/chromedriver.zip https://storage.googleapis.com/chrome-for-testing-public/128.0.6613.84/linux64/chromedriver-linux64.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    rm /tmp/chromedriver.zip

#№ Install ChromeDriver
#RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip && \
#    unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/ && \
#    chmod +x /usr/local/bin/chromedriver && \
#    rm /tmp/chromedriver.zip

# Установка Allure Commandline
RUN wget -qO- https://github.com/allure-framework/allure2/releases/download/2.17.3/allure-2.17.3.tgz | tar -xz -C /opt/ && \
    ln -s /opt/allure-2.17.3/bin/allure /usr/bin/allure

# Install xvfb for headless working
RUN apt-get install -y xvfb

## Clean apt cache
#RUN apt-get clean && rm -rf /var/lib/apt/lists/*
#
## Возвращаемся к пользователю Jenkins
#USER jenkins


# Очистка
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Возвращаемся к пользователю Jenkins
USER jenkins


docker run -d -p 8080:8080 -p 50000:50000 --restart=on-failure jenkins/jenkins
docker run -d -p 8080:8080 -p 50000:50000 --name my-jenkins-container my-jenkins-image
docker exec -it 77c2a571b93e cat /var/jenkins_home/secrets/initialAdminPassword
docker exec -u root -it 77c2a571b93e /bin/bash