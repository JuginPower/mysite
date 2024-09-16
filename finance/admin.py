from django.contrib import admin
from .models import Category, Activity, Keyword


admin.site.register([Category, Keyword, Activity])
