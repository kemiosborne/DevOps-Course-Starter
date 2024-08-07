# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.8+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.


## Setting up Trello Credentials
Create a Trello account
Create a API Token 
Fill in .env file




## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Running the Tests
To check the tests are passing, 
in the terminal session, run the tests: `poetry run pytest`

## Building and running the app via Containers
How to build the container image
```
docker build --target development --tag todo-app:dev .
docker build --target production --tag todo-app:prod .
```

How to run the container
```
docker run --publish 5000:5000 --env-file .env todo-app:prod
docker run --env-file ./.env -p 5100:5000 --mount "type=bind,source=$(pwd)/todo_app,target=/app/todo_app" todo-app:dev
```

Build the test container image
 
```
docker build --target test --tag todo-app:test
```

Run the test container 

```
docker run todo-app:test
```

## Pipelines

GitHub Actions pipelines are defined in the `.github/workflows` folder.

## Deploying the application

The application runs on Azure at https://osbornetodoapp.azurewebsites.net/

To update the application, first build the image locally:

```
docker build --target production --tag kemiosborne/todoapp .
```

Next push the image to Docker Hub:
```
docker push kemiosborne/todoapp
```

Lastly, make a POST request to the Azure App Service Webhook (this can be found under the App Service Deployment Center Settings)