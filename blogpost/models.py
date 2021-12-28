from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=220)
    content = models.TextField(max_length=1020, null= True)
    last_update = models.DateField(auto_now=True)