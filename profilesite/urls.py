from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = "profilesite"

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:section_id>/', views.profile_section_view, name="profile_section"),
    path('not_ready/', views.not_ready_view, name='not_ready'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
    ]
