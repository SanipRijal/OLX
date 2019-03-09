# OLX

## Cloning
**1. Using SSH keys**
`git clone git@github.com:SanipRijal/OLX.git`
**2. Using HTTPS**
`git clone https://github.com/SanipRijal/OLX.git`

## Create Virtual Environment
`virtualenv <path to your virtual environment> -p python3`

## Activate Virtual Environment
`source <path to your virtual environment>/bin/activate`

## Installing requirements required for this project
`pip install -r requirements.txt`

## Setting up database
**1. Install PostgreSQL10 in your system.**
Example:
`sudo apt-get install postgresql10`(ubuntu)
`sudo brew install postgresql10`(macOS)
**2. Create a database in postgresql with some name.**
Example:
`sudo -i -u postgres psql`
A postgres command line interface opens. Then:
`create database <database_name>;`
Close the postgres interface.
**3. Specify database in your settings.py file.**
`DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your database name',
        'USER': 'your postgres username',
        'PASSWORD': 'your postgres password',
        'HOST': '',
        'PORT': '',
    }
}`

## Running the system
Go to the folder that contains `manage.py` file.
`python manage.py runserver`
