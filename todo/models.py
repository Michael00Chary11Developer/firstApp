from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    priority = models.IntegerField()
    is_valid = models.BooleanField()

    def __str__(self) -> str:
        return f'{self.title} / is Done: {self.is_valid}'

    class Meta:
        db_table = "todos"
