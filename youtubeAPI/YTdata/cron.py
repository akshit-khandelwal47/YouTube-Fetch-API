import os
# Cron Job
from django_cron import CronJobBase, Schedule

# Google API
from googleapiclient.discovery import build
import apiclient

from .models import *
from youtubeAPI import settings
from datetime import datetime, timedelta


class CallYoutubeApi(CronJobBase):
    RUN_EVERY_MINS = 5  # runs after every 5 minutes

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'YTdata.call_youtube_api'    # a unique code

    def do(self):
        apiKeys = settings.GOOGLE_API_KEYS
        time_now = datetime.now()
        last_request_time = time_now - timedelta(minutes=5)

        #####################################################

        # A variable to check if a valid api key exists or not
        valid = False

        for apiKey in apiKeys:
            try:
                youtube = build("youtube", "v3", developerKey=apiKey)
                req = youtube.search().list(q="cricket", part="snippet", order="date", maxResults=50,
                                            publishedAfter=(last_request_time.replace(microsecond=0).isoformat()+'Z'))
                res = req.execute()
                print(res)
                valid = True
            except apiclient.errors.HttpError as err:
                code = err.resp.status
                if not(code == 400 or code == 403):
                    break

            if valid:
                break


        if valid:


            for item in res['items']:
                video_id = item['id']['videoId']
                publishedDateTime = item['snippet']['publishedAt']
                title = item['snippet']['title']
                description = item['snippet']['description']
                thumbnailsUrls = item['snippet']['thumbnails']['default']['url']
                channel_id = item['snippet']['channelId']
                channel_title = item['snippet']['channelTitle']
                print(title)
                VideoData.objects.create(
                    video_id=video_id,
                    title=title,
                    description=description,
                    channel_id=channel_id,
                    channel_title=channel_title,
                    publishedDateTime=publishedDateTime,
                    thumbnailsUrls=thumbnailsUrls,
                )