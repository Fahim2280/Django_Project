from django.http import HttpResponse
from django.shortcuts import render
from MainApp.models import Person

# Create your views here.


def home(request):
    persons = Person.objects.all()
    print(persons)
    return render(request, 'home.html', {'persons': persons})


