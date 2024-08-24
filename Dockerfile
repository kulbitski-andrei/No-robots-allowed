FROM  jenkins/jenkins:latest --platform linux/amd64
USER root
RUN apt update
RUN apt install -y wget git unzip build-essential software-properties-common python3 libnss3-dev libgdk-pixbuf2.0-dev libgtk-3-dev libxss-dev xvfb
RUN apt-get install python3-pip -y
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt install ./google-chrome*.deb
RUN wget https://storage.googleapis.com/chrome-for-testing-public/128.0.6613.84/linux64/chromedriver-linux64.zip
RUN unzip chromedriver-linux64.zip -d /usr/bin
ENV PATH=${PATH:+${PATH}:}/usr/bin/chromedriver-linux64