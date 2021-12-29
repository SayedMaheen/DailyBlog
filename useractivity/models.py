from django.db import models
# from django.contrib.contenttypes.models import ContentType
from bloguser.models import BlogUser
from blogpost.models import BlogPost


class UserActivity(models.Model):
    like_status = models.BooleanField(default=False)
    user_activity = models.DateTimeField(auto_now=True)
    current_user = models.ForeignKey(BlogUser , on_delete=models.CASCADE)
    current_post = models.OneToOneField(BlogPost, on_delete=models.CASCADE )
    comment = models.TextField(max_length=255, default="No Comments")
    
    def __str__(self) -> str:
        return self.current_post ,  self.current_user.username

    

