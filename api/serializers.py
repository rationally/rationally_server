from api.models import Topic, Alternative
from rest_framework import serializers
from django.contrib.auth.models import User, Group


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class TopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topic
        fields = ('url', 'name', 'state', 'description', 'date_modified', 'date_created')


class AlternativeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alternative
        fields = ('url', 'name', 'topic')
