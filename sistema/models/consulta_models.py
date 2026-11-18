from django.db import models # ORM do Django para declarar modelos no banco de dados
from django.utils import timezone # útil para gerar data/hora atual no projeto

from medico_models import Medico
from paciente_models import Paciente

# Modelo que representa uma consulta
# atributos => id do paciente, id do médico, data/hora da consulta, ativa (True/False), observação, status (Agendada (padrão), Confirmada, Cancelada, Realizada)
class Consulta(models.Model):
    paciente_id = models.ForeignKey(Paciente, on_delete=models.CASCADE) # Chave estrangeira
    medico_id = models.ForeignKey(Medico, on_delete=models.CASCADE) # Chave estrangeira
    data_consulta = models.DateTimeField(default=timezone.now) # Data/hora da consulta
    ativa = models.BooleanField(default=True) # Campo de exclusão lógica
    observacao = models.TextField(blank=True) # Anotação opcional
    status = models.CharField(
        default='A',
        max_length=1,
        choices=[
            ('A', 'Agendada'),
            ('X', 'Cancelada'),
            ('C', 'Confirmada'),
            ('R', 'Realizada'),
        ]
    )