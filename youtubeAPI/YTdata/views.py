from django.shortcuts import render
from urllib import request, response
from googleapiclient.discovery import build
from django.http import HttpResponse
def home(request):
   
    try:
        print(request.META.get('HTTP_REFERER'))

        api_key = 'AIzaSyAmYqCK5EG67gqQq1nzU285D5s54tqAc8Q'

        youtube = build('youtube','v3', developerKey=api_key)

        req = youtube.channels().list(
        part = ['snippet','contentDetails','statistics','id'],
        forUsername = 'GoogleDevelopers'

        )

        response = req.execute()
        print(response)
        context = {"response" : response}
        return render(request,'index.html',context)

    except:
        return HttpResponse('Wrong Url')

    

