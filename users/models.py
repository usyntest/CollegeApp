from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    year = models.IntegerField(default=0)
    course = models.CharField(default="None", max_length=250)
    clout = models.IntegerField(default=5)
    snapchat = models.CharField(null=True, blank=True, max_length=250)
    instagram = models.CharField(null=True, blank=True, max_length=250)


    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} Year - {self.year} Course - {self.course} Clout - {self.clout}"