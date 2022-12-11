from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Confession(models.Model):
    content = models.TextField(max_length=500)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"\"{self.content}\"\n{self.author}\n{self.date_posted.__str__()}"

class Alert(models.Model):
    content = models.TextField(max_length=500)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"\"{self.content}\"\n{self.author}\n{self.date_posted.__str__()}"
