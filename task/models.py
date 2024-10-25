
from django.db import models
from datetime import date
from category.models import Category


class task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    assign_date = models.DateField(default=date.today)
    category = models.ManyToManyField(Category, related_name='tasks')

    def __str__(self):
        return self.title
