from django.shortcuts import render
from django.http import HttpResponse

# View responsável pela tela inicial da consulta
def consulta_view(request):
    print('Página inicial da consulta funcionou')
    return HttpResponse('Página Inicial da Consulta')