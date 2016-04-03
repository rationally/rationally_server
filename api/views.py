from api.models import Topic, Alternative
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import TopicSerializer, AlternativeSerializer, UserSerializer, GroupSerializer


class TopicViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows decisions to be viewed or edited.
    """
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class AlternativeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows alternatives to be viewed or edited.
    """
    queryset = Alternative.objects.all()
    serializer_class = AlternativeSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer