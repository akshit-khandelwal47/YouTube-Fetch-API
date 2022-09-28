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

## API Version
The api for fetching youtube data through api is in the main branch.

## Alternative
To get the static response on a web page run the project of alternative-static branch.

1. In the terminal run ```git checkout alternative-static```
2. ```git pull```
3. Then run ```python manage.py runserver```

## Postman

In Postman use the youtube api endpoint and in the query params, pass the api key, pass a param part with values snippet, contentDetails, statistics, id and pass forUsername pass a channel name e.g. GoogleDevelopers.

Look in the body of response section, you will see the results.
