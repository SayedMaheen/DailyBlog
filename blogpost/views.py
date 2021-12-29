from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from blogpost.filters import BlogPostFilter
from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostViewSet(ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = BlogPostFilter
    search_fields = ['title']
    



