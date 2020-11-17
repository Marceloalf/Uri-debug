from .dicio import DESCRIPTION
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .lista.q1250 import input_q1250
from .lista.q1401 import input_q1401
from .lista.q2484 import input_q2484
from .lista.q2974 import input_q2974
from .lista.q2544 import input_q2544
from .lista.q2693 import input_q2693
from .lista.q2496 import input_q2496
from .lista.q2460 import input_q2460
from .lista.q2343 import input_q2343
from .lista.q2310 import input_q2310
from .lista.q2162 import input_q2162
from .lista.q2161 import input_q2161

# lista de questões
QUESTION = {
    1401: input_q1401,
    1250: input_q1250,
    2484: input_q2484,
    2974: input_q2974,
    2544: input_q2544,
    2693: input_q2693,
    2496: input_q2496,
    2460: input_q2460,
    2343: input_q2343,
    2310: input_q2310,
    2162: input_q2162,
    2161: input_q2161,
}

#l Lista com os nomes
Q_URI = [(1250, "1250 - Kiloman"),
        (1401, "1401 - Permutações"),
        (2484, "2484 - Abracadabra"),
        (2496, "2496 - Única chance"),
        (2544, "2544 - Kagebushin"),
        (2693, "2693 - Van"),
        (2974, "2974 - Fechadura"),
        (2460, "2460 - Fila"),
        (2343, "2343 - Caçadores de Mito"),
        (2310, "2310 - Voleibol"),
        (2162, "2162 - Picos e vales"),
        (2161, "2161 - Raiz quadrada"),
        ]

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
    context = {"input": input_q, "description":desc, 'title': title}

    if request.POST:
        input_q = function(forms(request))
        context["text"] = input_q
    return render(request, "html/questions.html", context)

def forms(request):
    form  = request.POST["textarea"].split("\n")
    form = list(map(str.strip, form))
    return form
