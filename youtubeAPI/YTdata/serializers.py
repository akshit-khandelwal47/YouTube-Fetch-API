from rest_framework import serializers 
from YTdata.models import *

class VideoDataSerializers(serializers.ModelSerializer):

    class Meta:
        model = VideoData
        fields = "__all__"
