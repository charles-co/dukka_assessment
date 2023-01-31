# Dukka Assessment Project Setup

## Table of Contents

- [Dukka Assessment Project Setup](#dukka-assessment-project-setup)
  - [Table of Contents](#table-of-contents)
  - [Local Development](#local-development)
    - [Run project locally with docker](#run-project-locally-with-docker)

## Local Development

1. Clone project repo
2. Install docker and docker-compose
3. Add docker to sudo group to use docker without sudo
4. Install pre-commit in your global environment

        pip install pre-commit

5. Install the git hook scripts

        cd <project_directory>
        pre-commit install

### Run project locally with docker

- Start the server

        docker-compose -f local.yml up --build

- Run commands inside the container

        docker-compose -f local.yml run --rm django <command>
    EX:

        - docker-compose -f local.yml run --rm django python manage.py makemigrations # To create the migration files
        - docker-compose -f local.yml run --rm django python manage.py migrate # To migrate the database
        - docker-compose -f local.yml run --rm django python manage.py createsuperuser # To create super user
        - docker-compose -f local.yml run --rm django pytest # For testing

- Run tests

        docker-compose -f local.yml run --rm django pytest
        docker-compose -f local.yml run --rm django pytest dukka_assessment/users/tests/ # To run tests in this folder only
