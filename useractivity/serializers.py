from django.db import models
from rest_framework import serializers

from bloguser.models import User
from .models import UserActivity



class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserActivity
        fields = ['id','like_status','current_user','current_post','comment']
    
   