from django.db import models
from .assignee import Assignee
from .group import Group

class Task(models.Model):
    class Status(models.IntegerChoices):
        created = (0, 'Created')
        assigned = (1, 'Assigned')
        done = (2, 'Done')


    status = models.IntegerField(choices=Status.choices)
    key = models.CharField(max_length=64)
    description = models.TextField()
    dod = models.TextField()
    assignee = models.ForeignKey(Assignee, null = True, on_delete=models.SET_NULL)
    group = models.ForeignKey(Group, null = True, on_delete=models.SET_NULL)

