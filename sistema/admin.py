from django.contrib import admin
from sistema import models

@admin.register(models.Paciente) # Registrando a classe Paciente no portal do python
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone', 'ativo',)

@admin.register(models.Medico) # Registrando a classe Medico no portal do python
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone', 'especialidade', 'crm', 'ativo',)

@admin.register(models.Consulta) # Registrando a classe Consulta no portal do python
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('id', 'paciente_id', 'medico_id', 'status',)