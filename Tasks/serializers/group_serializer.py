from Tasks.models import Group
from rest_framework import serializers


class Group_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        exclude = ()