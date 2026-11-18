from django.shortcuts import render
#from django.http import HttpResponse
from sistema.models import Paciente

# GLOBAL -> refere-se a uma página inteira
# PARTIAL -> refere-se a uma parte da página (header, footer, form)
# MVT -> Templates/global/base.html

# View responsável pela tela inicial do paciente
def index_paciente(request):
    return render(
        request,
        'index.html',
        )

# View responsável por listar todos os pacientes
# def listar_pacientes(request):
#     pacientes = Paciente.objects.all() # [ob1, obj2, obj3]

#     context = {
#         'pacientes': pacientes,
#     }

#     return render(
#         request,
#         'paciente/listar.html',
#         context,)