from django.shortcuts import render
from .models import Pomen

def index(request):
    return render(request, 'index.html')
