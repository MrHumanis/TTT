from Tasks.models import Task
from Tasks.serializers import Task_Serializer
from rest_framework import viewsets


class Task_Viewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = Task_Serializer