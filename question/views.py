from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .dicio import DESCRIPTION
from .lista.q1250 import input_q1250
from .lista.q1401 import input_q1401
from .lista.q2484 import input_q2484

# lista de questões
QUESTION = {
    1401: input_q1401,
    1250: input_q1250,
    2484: input_q2484,
}

#l Lista com os nomes
Q_URI = [(1250, "1250 - Kiloman"),
        (1401, "1401 - Permutações"),
        (2484, "2484 - Abracadabra"),]

# Pagina inicial
def home(request):
    return render(request, "html/index.html", {"text": Q_URI})

# Função para procurar o nome da questão. Caso não tenha, retorna string vazia
def search_by_id(id):
    for i in Q_URI:
        id_vector, name = i

        if id_vector == id:
            return name
    return ''

def questoes(request, question_id):
    # Função correspondente à requestão
    function = QUESTION[question_id]

    # Variáveis a serem renderizadas no site  
    input_q = ''
    desc = DESCRIPTION[question_id]
    title = search_by_id(question_id)

    #tupla enviada pro site
    context = {"text": input_q, "description":desc, 'title': title}

    if request.POST:
        input_q = function(forms(request))
        context["text"] = input_q
    return render(request, "html/questions.html", context)

def forms(request):
    form  = request.POST["textarea"].split("\n")
    form = list(map(str.strip, form))
    return form
