from django.db import models
from rest_framework import serializers
from blogpost.models import BlogPost
from bloguser.models import BlogUser


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id','title','content','last_update','author']
    
    # last_update = serializers.DateTimeField(auto_now = True