from django.db import models
from bloguser.models import BlogUser

class BlogPost(models.Model):
    title = models.CharField(max_length=220)
    content = models.TextField(max_length=1020)
    last_update = models.DateTimeField(auto_now=True)
    author =  models.ForeignKey(BlogUser, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['-last_update']
   