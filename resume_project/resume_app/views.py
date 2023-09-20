from django.shortcuts import render
from .models import Resume

def resume(request):
    # Fetch the resume data from the database
    resume = Resume.objects.first()

    return render(request, 'resume.html', {'resume': resume})
