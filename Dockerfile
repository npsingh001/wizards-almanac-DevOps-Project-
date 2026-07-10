# Example Jenkins Dockerfile, modify this to complete the challenge
FROM jenkins/jenkins:lts

USER root

RUN apt-get update && \
    apt-get install -y docker.io docker-compose && \
    rm -rf /var/lib/apt/lists/*

USER jenkins


