from django.shortcuts import render
from django.http import HttpResponse

# View responsável pela tela inicial do médico
def medico_view(request):
    print('Página inicial do médico funcionou')
    return HttpResponse('Página Inicial do Médico')