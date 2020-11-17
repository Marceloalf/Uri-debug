from .q_list import Q_URI
from .dicio import DESCRIPTION
from .functions import QUESTION
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def search_by_id(id):
    for i in Q_URI:
        id_vector, name = i

        if id_vector == id:
            return name
    return ''


def home(request):
    return render(request, "html/index.html", {"text": Q_URI})


def question_page(request, question_id):
    output = ''
    desc = DESCRIPTION[question_id]
    function = QUESTION[question_id]
    title = search_by_id(question_id)

    #tupla enviada pro site
    context = {"input": output, "description":desc, 'title': title}

    #Pegando o formulário
    if request.POST:
        output = function(forms(request))
        context["text"] = output
    return render(request, "html/questions.html", context)


def error_verification(request, question_id):
    try:
        return question_page(request, question_id)
    except KeyError:
        return render(request, "html/error.html", {'error': "Questão inválida"})


def forms(request):
    form  = request.POST["textarea"].split("\n")
    form = list(map(str.strip, form))
    return form
