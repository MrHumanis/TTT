from Tasks.models import Group
from Tasks.serializers import Group_Serializer
from rest_framework import viewsets


class Group_Viewset(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = Group_Serializer