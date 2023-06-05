from django.db import models
from django.contrib.auth.models import User



class Home(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=False)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
