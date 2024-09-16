from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ProfileSection


def index(request):
    section = get_object_or_404(ProfileSection, id=1)
    return render(request, '1/', {'section':section})


def profile_section_view(request, section_id):
    section = get_object_or_404(ProfileSection, id=section_id)

    if not section.is_published and not request.user.is_authenticated:
        return render(request, 'not_ready.html')
    
    return render(request, 'profile_section.html', {'section': section})


@login_required
def restricted_section(request):
    return render(request, 'restricted_section.html')


def not_ready_view(request):
    return(request, 'not_ready.html')