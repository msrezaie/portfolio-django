from django.contrib import admin
from . models import Project, Tag, Profile

admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Tag)