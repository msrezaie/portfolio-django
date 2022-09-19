from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_index, name='projects_list'),
    # path('projects/<int:pk>', views.project_detail, name='projects_detail')
]