from django.contrib.auth.models import User, Group
from rest_framework import serializers
from Blog.models import blog
from News.models import news
from Youtube.models import youtube
from User.models import Profile

#from taggit.serializers import (TagListSerializerField, TaggitSerializer)

class blogSer(serializers.ModelSerializer ):
    #tags = TagListSerializerField()

    class Meta:
        model = blog 
        fields = "__all__"
  

class newsSer(serializers.ModelSerializer ):
   # tag = TagListSerializerField()
    class Meta:
        model = news
        fields = "__all__"

class youtubeSer(serializers.ModelSerializer):
    class Meta:
        model = youtube
        fields = "__all__"