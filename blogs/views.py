from django.shortcuts import render, redirect, get_list_or_404
from profilesite.models import Bouncer
from .models import Category


title = "Blogwebseite"

def check_permission():
    bouncer = Bouncer.objects.filter(purpose='bl').first()
    return bouncer.permission if bouncer else False


def index(request):
    if not check_permission():
        return redirect('blogs:not_ready')
    
    cats = get_list_or_404(Category)
    return render(request, "blogs/index.html", {"cats": cats})


def not_ready(request):
    return render(request, 'not_ready.html', {'title': title})