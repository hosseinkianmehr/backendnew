from django.shortcuts import render
from rest_framework import generics
from Blog.models import blog
from Youtube.models import youtube
from News.models import news
from .serializers import blogSer ,newsSer, youtubeSer


# home
# last yotube film / last blog post 
# The last 3 are blog posts 
# The last 6 are youtube posts
# The last 3 are news posts
from rest_framework.response import Response
from rest_framework.views import APIView
class Home(APIView):
    def get(self, request):
        bloglist = blog.objects.all()
        newslist = news.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializerblog = blogSer(bloglist[:3], many=True)
        serializernews = newsSer(newslist[:3], many=True)
        return Response({"blog": serializerblog.data,"news": serializernews.data})

# list blog (Titel / image / Summary)
class listblog(generics.ListAPIView):
    queryset= blog.objects.all()
    serializer_class = blogSer

# blog
# The last 3 are tag posts 
class detailblog(generics.RetrieveAPIView):
    queryset= blog.objects.all()
    serializer_class = blogSer

# list youtube (Titel / image / Summary)
class listyoutube(generics.ListAPIView):
    queryset= youtube.objects.all()
    serializer_class = youtubeSer

# youtube
# The last 3 are tag posts 
class detailyoutube(generics.RetrieveAPIView):
    queryset= youtube.objects.all()
    serializer_class = youtubeSer

# list news (Titel / image / Summary)
class listnews(generics.ListAPIView):
    queryset= news.objects.all()
    serializer_class = newsSer

# news
# The last 3 are tag posts 
class detailnews(generics.RetrieveAPIView):
    queryset= news.objects.all()
    serializer_class = newsSer