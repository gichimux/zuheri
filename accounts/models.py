from django.db import models

from django.contrib.auth.models import User 

class Customer(models.Model):
    user = models.ForeignKey(User, related_name='customers', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name
        