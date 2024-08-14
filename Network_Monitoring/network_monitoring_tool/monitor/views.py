from django.shortcuts import render
from .models import Vulnerability


def index(request):
    vulnerabilities = Vulnerability.objects.all()
    return render(request, 'monitor/index.html', {'vulnerabilities': vulnerabilities})
