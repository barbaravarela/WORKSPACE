from django.urls import path
from sistema.views import *

urlpatterns = [
    path('paciente/', index_paciente), # vollmed.com/paciente
    #path('paciente_novo/'), # vollmed.com/paciente_novo
    #path('paciente/perfil/<int:paciente_id>'), # vollmed.com/paciente/perfil/<int:paciente_id>
    #path('paciente/listagem', listar_pacientes) # vollmed.com/paciente/listagem
]