from django.shortcuts import render

from django.http import HttpResponse
from django.urls import path


def index(request):
    # Ez jöhetne adatbázisból
    elements = ["Egy", "Ketto", "Harom"]

    page = []
    page.append("""
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Tabor teszt</title>
  <link href="/static/tabor.css" rel="stylesheet">
  <link rel="shortcut icon" type="image/png" href="/static/logo-small-256.png">
</head>

<body>
  <img src="/static/logo-small-256.png" alt="Techtabor"/>
  <h1>Elemek listája:</h1>
  <ul>
""")
    
    for element in elements:
        page.append("    <li>{}</li>\n".format(element))
        
    page.append("  </ul>\n</body>")

    return HttpResponse("".join(page))
    
urlpatterns = [
    path('', index, name='index'),
]