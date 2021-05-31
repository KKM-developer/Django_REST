from django.db import models
from users.models import CustomUser

class Project(models.Model):
    email = models.ForeignKey(
        CustomUser, to_field='email', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = 'CustomUser'

class TODO(models.Model):
    email = models.ForeignKey(
        CustomUser, to_field='email', on_delete=models.CASCADE, null=True, blank=True)
    title = models.ForeignKey(
        Project, to_field='title', on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
