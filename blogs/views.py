from django.shortcuts import render, get_list_or_404
from .models import Category


def index(request):
    cats = get_list_or_404(Category)
    return render(request, "blogs/index.html", {"cats": cats})


