from Tasks.views import Assignee_Viewset, Task_Viewset, Group_Viewset
from django.urls import path, include
from rest_framework import routers


router = routers.DefaultRouter()
router.register('assignee', Assignee_Viewset, 'assignee')
router.register('task', Task_Viewset, 'task')
router.register('group', Group_Viewset, 'group')


urlpatterns = [
    path('', include(router.urls)),
]