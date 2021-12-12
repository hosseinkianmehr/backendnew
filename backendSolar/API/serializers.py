from django.contrib.auth.models import User, Group
from rest_framework import serializers
from Blog.models import blog
from News.models import news
from Youtube.models import youtube
from User.models import Profile
from TagAndComment.models import tag

#$$$$$$$$tag handel
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = tag
        fields = '__all__'
#$$$$$$$$$$$$$$$$$$
class blogSer(serializers.ModelSerializer ):
    tag  = TagSerializer(many=True, read_only=True)
    class Meta:
        model = blog 
        fields = "__all__"

class newsSer(serializers.ModelSerializer ):
    tag  = TagSerializer(many=True, read_only=True)
    class Meta:
        model = news
        fields = "__all__"

class youtubeSer(serializers.ModelSerializer):
    tag  = TagSerializer(many=True, read_only=True)
    class Meta:
        model = youtube
        fields = "__all__"