FROM python:3.9.1-slim-buster

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git && \
    pip install pip --upgrade

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENV GITHUB_URL ""
ENV GITHUB_REPO ""
ENV GITHUB_BRANCH ""
ENV YAML_PATH ""
ENV TARGET_KEY ""
ENV NEW_VALUE ""
ENV COMMIT_MESSAGE "Update yaml from github-yaml-modifier"
ENV COMMIT_AUTHOR "bot <bot@bot.com>"

ENTRYPOINT sh entrypoint.sh ${GITHUB_URL} ${GITHUB_REPO} ${GITHUB_BRANCH} \ 
            ${GITHUB_BRANCH} ${YAML_PATH} ${TARGET_KEY} ${NEW_VALUE} \ 
            ${COMMIT_MESSAGE} ${COMMIT_AUTHOR}
CMD python main.py