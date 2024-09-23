from django.shortcuts import render, redirect, get_object_or_404
from .models import Bouncer


def check_permission():
    bouncer = Bouncer.objects.filter(purpose='pr').first()
    return bouncer.permission if bouncer else False


def index(request):
    if not check_permission():
        return redirect('profilesite:not_ready')
    return render(request, 'index.html')


def about(request):
    if not check_permission():
        return redirect('profilesite:not_ready')
    return render(request, 'profilesite/about.html')


def resume(request):
    if not check_permission():
        return redirect('profilesite:not_ready')
    return render(request, 'profilesite/resume.html')


def projects(request):
    if not check_permission():
        return redirect('profilesite:not_ready')
    return render(request, 'profilesite/projects.html')


def not_ready(request):
    return render(request, 'profilesite/not_ready.html')