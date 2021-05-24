from django.db import models

class Project():
    pass

class TODO():
    title = models.CharField(max_length=30)
    title_text = models.TextField(max_length=300)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

