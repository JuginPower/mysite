from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = "profilesite"

urlpatterns = [
    path('', views.index, name="index"),
    path('not_ready/', views.not_ready, name='not_ready'),
    path('about/', views.about, name='about'),
    path('resume/', views.resume, name='resume'),
    path('projects/', views.projects, name='projects')
    ]
