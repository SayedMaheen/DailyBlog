from django_filters.rest_framework import FilterSet
from .models import BlogPost


class BlogPostFilter(FilterSet):
    class Meta:
        model = BlogPost
        fields = {
            'last_update':['gt','lt']
        }

