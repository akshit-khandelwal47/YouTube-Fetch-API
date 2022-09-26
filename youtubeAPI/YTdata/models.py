from django.db import models

# Create your models here.
# Video title, description, publishing datetime, thumbnails URLs and any other fields you require
class VideoData(models.Model):
    video_id = models.CharField(null=False,max_length=250, blank=False )
    video_title = models.CharField(null=True,max_length=300)
    description = models.CharField(null=True,blank=True,max_length=1000)
    published_datetime = models.DateTimeField() 
    thumbnail_urls = models.URLField()
    channel_id = models.CharField(null=False,blank=False,max_length=500)
    channel_title = models.CharField(null=False,blank=False,max_length=500)
