# the-front-page

*Version: 1.0*

## How to get started on your local development environment.
#### Prerequisites:

* git
* python 2.7.x
* virtualenv
* mysql

### Create project directory and environment

* `mkdir the-front-page && cd the-front-page`
* `virtualenv env`
* `source env/scripts/activate` *Activate the environment (each time you start a session working with the code)*

*Obtain source code and clone into crawler directory*
* `git clone https://github.com/lestrato/the-front-page.git crawler`
* `cd crawler`

*Your Directory structure will look like this:*
```
the-front-page
├── crawler
│   ├── crawler
│   ├── mainsite
│   ├── static
├── env
```

### Install requirements
*from within the-front-page/crawler directory*
* `pip install -r requirements.txt`

### Customize local settings to your environment
* cp crawler/settings.py.example crawler/settings.py
* Edit the crawler/settings.py file and insert local credentials for DATABASES

### Migrate databases, build front-end components
* `./manage.py migrate`

### Run a server locally for development
* `./manage.py runserver`
* Navigate to http://localhost:8000/
