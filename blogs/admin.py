from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Name und Beschreibung", {"fields": ["name", "description"]})
        ]

admin.site.register(Category, CategoryAdmin)
