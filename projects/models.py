from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    technology = models.CharField(max_length=100)
    image = models.FilePathField(path="/img")