from django.shortcuts import render

from django.http import HttpResponse
from django.urls import path


def index(request):
    elements = ["Egy", "Ketto", "Harom"]

    page = []
    page.append("""
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Tabor teszt</title>
</head>

<body>
  <p>Elemek listája:</p>
  <ul>
""")
    
    for element in elements:
        page.append("    <li>{}</li>\n".format(element))
        
    page.append("  </ul>\n</body>")

    return HttpResponse("".join(page))
    
urlpatterns = [
    path('', index, name='index'),
]