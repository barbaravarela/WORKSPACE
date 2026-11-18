from django.urls import path
from sistema.views import medico_view

urlpatterns = [
    path('medico/', medico_view), # vollmed.com/medico
    path('medico_novo/'), # vollmed.com/medico_novo
    path('medico/perfil/<int:medico_id>'), # vollmed.com/medico/perfil/<int:medico_id>
    path('medico/listagem') # vollmed.com/medico/listagem
]