from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .lista.q1250 import input_q1250
from .lista.q1401 import input_1401


QUESTION = {
    1401: input_1401,
    1250: input_q1250
}

def home(request):
    q_uri = [(1250, '1250 - Kiloman'),
             (1401, '1401 - permutações'),]

    return render(request, "html/index.html", {'text': q_uri})

def questoes(request, question_id):
    input_q = []
    function = QUESTION[question_id]

    if request.POST:
        input_q = function(forms(request))

    return render(request, "html/{}.html".format(question_id), {"text":input_q})

def forms(request):
    form  = request.POST["textarea"].split("\n")
    form = list(map(str.strip, form))
    return form