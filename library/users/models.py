from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()
    email = models.EmailField(primary_key=True, max_length=100, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email
