from django.db import models


class Title(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    about = models.TextField()
