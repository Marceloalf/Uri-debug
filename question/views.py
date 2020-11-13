from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .dicio import DESCRIPTION
from .lista.q1250 import input_q1250
from .lista.q1401 import input_1401


QUESTION = {
    1401: input_1401,
    1250: input_q1250
}

Q_URI = [(1250, "1250 - Kiloman"),
        (1401, "1401 - Permutações"),]

def home(request):
    return render(request, "html/index.html", {"text": Q_URI})

def questoes(request, question_id):
    input_q = []
    
    function = QUESTION[question_id]
    desc = DESCRIPTION[question_id]

    context = {"text": input_q, "description":desc, 'title': question_id}

    if request.POST:
        input_q = function(forms(request))
        context["text"] = input_q
    return render(request, "html/questions.html", context)

def forms(request):
    form  = request.POST["textarea"].split("\n")
    form = list(map(str.strip, form))
    return form
