from Tasks.models import Assignee
from rest_framework import serializers


class Assignee_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Assignee
        exclude = ()