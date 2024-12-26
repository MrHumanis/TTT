from Tasks.models import Assignee
from Tasks.serializers import Assignee_Serializer
from rest_framework import viewsets


class Assignee_Viewset(viewsets.ModelViewSet):
    queryset = Assignee.objects.all()
    serializer_class = Assignee_Serializer