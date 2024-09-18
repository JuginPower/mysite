from django.shortcuts import render, redirect, get_object_or_404
from .models import Bouncer


def check_permission():
    bouncer = Bouncer.objects.first()  # Annahme: Es gibt nur einen Bouncer
    return bouncer.permission if bouncer else False


def index(request):
    if not check_permission():
        return redirect('profilesite:not_ready')
    return render(request, 'index.html')


def about(request):
    if not check_permission():
        return redirect('profilesite:not_ready')
    return render(request, 'about.html')


def resume(request):
    if not check_permission():
        return redirect('profilesite:not_ready')
    return render(request, 'resume.html')


def projects(request):
    if not check_permission():
        return redirect('profilesite:not_ready')
    return render(request, 'projects.html')


def not_ready(request):
    return render(request, 'not_ready.html')