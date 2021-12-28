from django.db import models
from bloguser.models import BlogUser
from blogpost.models import BlogPost

# class for timeline activity, which tracks 
# time of like, post, comment, etc for an individual
# class UserActivity(models.Model);


class LikedPost(models.Model):
    status = models.IntegerField( default=0)
    like_activity = models.DateTimeField(auto_now=True)
    liked_by = models.OneToOneField(BlogUser, on_delete=models.CASCADE)
    liked_post = models.OneToOneField(BlogPost, on_delete=models.CASCADE )


class CommentOn(models.Model):
    comment = models.TextField(max_length=255, default="No Comments")
    commenter = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    comment_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE )
    comment_activity = models.DateTimeField(auto_now=True)


