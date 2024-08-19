from django.db import models


class Todo(models.Model):
    # max_lebgh is require
    title = models.CharField(max_length=100)
    body = models.TextField()
    create = models.DateTimeField()
