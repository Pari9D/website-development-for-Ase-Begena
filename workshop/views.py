from django.shortcuts import render
from .models import Bagan

def home(request):
    bagans = Bagan.objects.all()  # Fetch all Begenas
    return render(request, 'home.html', {'bagans': bagans})