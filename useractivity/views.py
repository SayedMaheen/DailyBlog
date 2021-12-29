
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from .models import UserActivity
from .serializers import UserActivitySerializer


class UserActivityViewSet(ModelViewSet):
    queryset = UserActivity.objects.all()
    serializer_class = UserActivitySerializer





