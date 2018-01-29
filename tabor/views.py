from django.shortcuts import render

from django.urls import path
from django.conf import settings


def index(request):
    print(settings.BASE_DIR)
    
    elements = ["Egy", "Ketto", "Harom"]
    
    context = {
        'elements': elements,
    }

    return render(request, 'tabor/index.html', context)
    
urlpatterns = [
    path('', index, name='index'),
]