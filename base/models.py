from django.db import models
import uuid


class Project(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    # unique attribute meaning: no other value can have
    # the same value as the value of the following 'id'
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title
