from Tasks.models import Task
from rest_framework import serializers


class Task_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        exclude = ()