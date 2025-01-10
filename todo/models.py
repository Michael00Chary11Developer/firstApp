from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Todo(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    priority = models.IntegerField()
    is_valid = models.BooleanField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='todos')

    def __str__(self) -> str:
        return f'{self.title} / is Done: {self.is_valid} / f{self.user}'

    class Meta:
        db_table = "todos"


# رابطه‌های یک‌به‌چند در Django

# در Django، وقتی از ForeignKey استفاده می‌کنید، رابطه‌ای از نوع یک‌به‌چند را بین دو مدل تعریف می‌کنید:

#     مدل مبدا (یک‌به‌چند): مدلی که ForeignKey را تعریف می‌کند و هر رکورد آن می‌تواند به یک رکورد از مدل مقصد مرتبط باشد.
#     مدل مقصد (چندین): مدلی که به آن ForeignKey ارجاع داده می‌شود و می‌تواند چندین رکورد از مدل مبدا را داشته باشد.