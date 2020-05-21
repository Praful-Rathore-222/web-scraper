# web-scraper

Fetch the LinkedIn profiles by using web scraping.

The project contains REST API's which can be used to scrap linkedin profiles, retrieve the list of scraped profiles or retrieve the detail of specific employee profile.

# Technology Stack
We have used,
```
1. Python 3
2. Django REST Framework
3. sqlite3 Database
4. Google Chrome v.83.0.4103.61    
5. Google Chrome driver v.83.0.4103.61
4. Docker
5. docker-compose
```

# Project Structure:

```
├── API.md: API documentation
├── Assumption.md: asumption made for tracxn scraper app
├── config.ini.example: example file for config.ini to store linkedin credentials
├── linkedin_scraper
│   ├── admin.py
│   ├── apps.py
│   ├── chromedriver_linux64
│   ├── fixtures : contains inital data to load
│   ├── __init__.py
│   ├── migrations: database migrations
│   ├── models.py: database models for linkedin scraper app
│   ├── serializers.py: serializers for above models
│   ├── tests.py: test cases for view
│   ├── urls.py: url endpoints of linkedin scraper app
│   ├── utilities.py: Utility functions used in views
│   └── views.py: These views are called by API endpoints
├── Makefile: initial commands
├── manage.py
├── README.md: documentation file
├── requirements.txt: requirements needs to be install
├── task.md:task description
├── tracxn_scraper
│   ├── admin.py
│   ├── apps.py
│   ├── fixtures: contains inital data to load
│   ├── __init__.py
│   ├── migrations: database migrations
│   ├── models.py: database models for tracxn scraper app
│   ├── serializers.py: serializers for above models
│   ├── tests.py: test cases for view
│   ├── urls.py: urls for tracxn scraper app
│   └── views.py: These views are called by API endpoints
└── webscraper
    ├── asgi.py
    ├── __init__.py
    ├── settings.py: settings file for the project.
    ├── urls.py: base urls for apps of the projects
    └── wsgi.py
```

# Running Locally

First, clone the repository to your local machine:

```
git clone https://github.com/fulltostack/web-scraper

cd web-scraper
```

Install the requirements:

```
pip install -r requirements/dev.txt
```


Create the .env file to the root directory of the project.
You can refer this example file-
 

### [.env.example](./.env.example) 


Create the config.ini file to the root directory of the project.
You can refer this example file- 


### [config.ini.example](./config.ini.example)

Apply the migrations:

```
python manage.py migrate
```

Load the initial data:

```
python manage.py loaddata companies
```
Create administrator/super user:
```
python manage.py createsuperuser 


Note: It will prompt to enter username, email and password one by one. Please remember the username and password, it will be
used to login admin area or to hit an API to scrap/refresh the linkedin profiles.
```


Finally, run the development server:

```
python manage.py runserver
```

` The site will be available at 127.0.0.1:8000. `

## Linting:

```
make lint
```

## APIs Details

See documentation [here.](./API.md)

## Testing:

```
python manage.py test
```

### Further improvements
Along with the linkedin, tracxn data can be scraped, stored and retrieved in similar fashion. 

