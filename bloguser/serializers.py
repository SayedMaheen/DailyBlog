from django.db import models
from rest_framework import serializers
from blogpost.models import BlogPost
from bloguser.models import BlogUser


class BlogUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogUser
        fields = ['id','first_name','last_name','email','username']
    
    # last_update = serializers.DateTimeField(auto_now = True