# crud-cbv

> [default-007](https://github.com/default-007)

# Description

This project showcases how to perform CRUD operations on class Based views

## Live Link

Click [View Site](https://awwwards-007.herokuapp.com/) to visit the site

## Screenshots

###### Home page

<img src="https://raw.githubusercontent.com/default-007/awwwards/master/static/images/landing.png">
 
 ###### Rating of a post
<img src="https://raw.githubusercontent.com/default-007/awwwards/master/static/images/profile.png">

## User Story

- A user can view posted projects and their details.
- A user can post a project to be rated/reviewed.
- A user can rate/ review other users' projects.
- Search for projects.
- View projects overall score.
- A user can view their profile page.

## Setup and Installation

To get the project .......

##### Cloning the repository:

```bash
https://github.com/default-007/crud-cbv.git
```

##### Navigate into the folder and install requirements

```bash
cd crud-cbv pip install -r requirements.txt
```

##### Install and activate Virtual

```bash
- python3 -m venv virtual - source virtual/bin/activate
```

##### Install Dependencies

```bash
pip install -r requirements.txt
```

##### Setup Database

SetUp your database User,Password, Host then make migrate

```bash
python manage.py makemigrations instagram
```

Now Migrate

```bash
python manage.py migrate
```

##### Run the application

```bash
python manage.py runserver
```

##### Testing the application

```bash
python manage.py test
```

Open the application on your browser `127.0.0.1:8000`.

### Api Endpoints

- https://crud-cbv.herokuapp.com/api/users/

## Technology used

- [Python3.6](https://www.python.org/)
- [Django 4.0](https://docs.djangoproject.com/en/4.0/)
- [Heroku](https://heroku.com)

## Known Bugs

- There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information

If you have any question or contributions, please email me at [brianokola@gmail.com]

## License

- [![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](https://github.com/default-007/crud-cbv/master/LICENSE)
- Copyright (c) 2019 **Brian Otieno**
