
from django.shortcuts import render, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse
from rest_framework import status
# from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer
from blogpost import serializers


# class BlogPostList(ListAPIView):
#     queryset = BlogPost.objects.all()
#     serializer = BlogPostSerializer(queryset, many =True)
#     filter_backends = (DjangoFilterBackend,)
#     filter_fields =('id', )

@api_view(['GET','POST'])
def blog_list(request):
    if request.method == 'GET':
        queryset = BlogPost.objects.all()
        serializer = BlogPostSerializer(queryset, many =True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BlogPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
       

@api_view(['GET','PUT','PATCH','DELETE'])
def blog_content(request, id):
    post = get_object_or_404(BlogPost,pk=id)
    if request.method == 'GET':
        serializer = BlogPostSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BlogPostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = BlogPostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)