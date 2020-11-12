from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .lista.q1250 import KiloMan

def home(request):
    q_uri = ['1250 - Kiloman',
             '1401 - Permutações',]

    return render(request, "Questions/index.html", {'text': q_uri})

def q_1250(request):

    input_q = []
    if request.POST:
        input_q = request.POST['textarea'].split('\r\n')
        
        i = input_q[0]
        input_q.remove(input_q[0])
        
        print(i)
    return render(request, "Questions/1250.html", {'text': input_q})