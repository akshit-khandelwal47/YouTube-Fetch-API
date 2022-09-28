# YouTube Fetch API

## Pre-requisites
1. Python-3.7.4
2. Django-3.2.15

## Installation Guide
1.  Go to your project folder and in the terminal clone the repository using : ```git clone https://github.com/akshit-khandelwal47/Vidyo-Assingment.git```
2.  Now, for installing the requirements use the given command in the terminal: ```pip install -r requirements.txt```
3.  Go to settings.py -> search for GOOGLE_API_KEY and add your API Key in the array format as ```['API_KEY_1','API_KEY_2',...]```
4.  Get your API Key from [here](https://developers.google.com/youtube/v3/getting-started)
5.  In settings.py add CRON_CLASS by referring [here](https://django-cron.readthedocs.io/en/latest/installation.html)
6.  To run the server ```python manage.py runserver```

