# github-yaml-modifier

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

`github-yaml-modifier` is a simple command that edit the yaml file on GitHub.  

It can be utilized in the CI/CD pipeline. 
Specifically, I made this to make the CI/CD pipeline action easier in GitOps deployment strategy.

<br>

## Usage

Here is an example of use.

First of all, my GitHub repo has the following commits

![](https://user-images.githubusercontent.com/31306282/122244304-bdba0800-ceff-11eb-9f34-9ce848266653.png)
![](https://user-images.githubusercontent.com/31306282/122244680-05d92a80-cf00-11eb-86b9-c6dd66eb17c4.png)

Now, Let's run the program like this.

```bash
$ docker run \
-e GITHUB_URL=https://heumsi:{MY_ACCESS_TOKEN}@github.com/heumsi/playground.git \
-e GITHUB_BRANCH=master \
-e YAML_PATH=test.yaml \
-e TARGET_KEY=app.image \
-e NEW_VALUE=newImageName \
-e COMMIT_MESSAGE="Update yaml from github-yaml-modifier" \
-e COMMIT_AUTHOR="bot <bot@bot.com>" \
-e LOG_LEVEL=INFO \
heumsi/github-yaml-modifier
```

After that, you can see that there is a commit that modified the yaml file on GitHub like this.

![](https://user-images.githubusercontent.com/31306282/122244912-3a4ce680-cf00-11eb-8370-8511a3666585.png)
![](https://user-images.githubusercontent.com/31306282/122244947-420c8b00-cf00-11eb-8508-8e34d627eea3.png)

<br>

## Parameters

| Environment Variable | Description                                                  | Required | Default |
| -------------------- | ------------------------------------------------------------ | -------- | ------- |
| GITHUB_URL           | Your GitHub repository url with access token<br />`ex. https://heumsi:{MY_ACCESS_TOKEN}@github.com/heumsi/playground.git` | `True`   |         |
| GITHUB_BRANCH        | Your GitHub repository branch<br />`ex. main`                | `True`   |         |
| YAML_PATH            | Path of yaml file in GitHub repository to be modified<br />`ex. test.yaml` | `True`   |         |
| TARGET_KEY           | Key in yaml to be modified<br />`ex. app.image`              | `True`   |         |
| NEW_VALUE            | Value to set<br />`ex. newImageName`                         | `True`   |         |
| COMMIT_MESSAGE       | Message of commit <br />`ex. 'Update yaml'`                  | `True`   |         |
| COMMIT_AUTHOR        | Author of commit<br />`ex. 'bot <bot@bot.com>'`              | `True`   |         |
| LOG_LEVEL            | Logging Level (`INFO`, `DEBUG`)                              | `False`  | `DEBUG` |


