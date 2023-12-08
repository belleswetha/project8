from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def philips(request):
    return HttpResponse('<h1> raina is the best player of circket teams</h1>')
