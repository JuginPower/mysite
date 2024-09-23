from django.urls import path
from . import views


app_name = "blogs"

urlpatterns = [
    path("", views.index, name="index"),
    path('not_ready/', views.not_ready, name='not_ready'),
    ]
