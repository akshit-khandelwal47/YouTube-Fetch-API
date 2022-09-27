from django.shortcuts import render
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from YTdata.models import *
from YTdata.serializers import *
from rest_framework import generics
from rest_framework.pagination import CursorPagination


class PaginationRes(CursorPagination):
    page_size = 25
    page_size_query_param = page_size
    max_page_size = 120

class YouTubeVid(generics.ListAPIView):
    
    search_field = ['video_title','description']
    filter_backends = (filters.SearchFilter,DjangoFilterBackend,filters.OrderingFilter)
    filterset_field = ['channel_id','channel_title']
    ordering = ('-published_datetime')
    queryset = VideoData.objects.all()
    serializer_class = VideoDataSerializers
    pagination_class = PaginationRes
