from django.urls import path
from . import views 
# from .views import BlogPostList

urlpatterns = [
    path('posts/', views.blog_list),
    path('posts/<int:id>/', views.blog_content),
]
