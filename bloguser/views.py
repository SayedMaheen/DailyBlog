from rest_framework.viewsets import ModelViewSet
from .models import BlogUser
from .serializers import BlogUserSerializer

class BlogUserViewSet(ModelViewSet):
    queryset = BlogUser.objects.all()
    serializer_class = BlogUserSerializer
    

