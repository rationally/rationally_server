from api.models import Decision, Alternative
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


class DecisionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Decision
        fields = ('url', 'name', 'modified_date')


class AlternativeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alternative
        fields = ('url', 'name', 'decision')