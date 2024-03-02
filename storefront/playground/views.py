from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sayHello (request):
    #inside this, you could pull data from a db, send emails, transform tthings, etc
    return HttpResponse("Hello World")

def sayHello2 (request):
    return render(request, 'hello.html', {'name': 'Aarish'})