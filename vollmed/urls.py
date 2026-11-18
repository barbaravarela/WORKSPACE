from django.contrib import admin
from django.urls import path, include

import sistema.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(sistema.urls)) # Preciso chamar as urls do app sistema
    # path('') # Preciso chamar as urls do app portal
]








# www.volllmed.online/
# www.volllmed.online/login/
# www.volllmed.online/


# MEDICO
# www.volllmed.online/medico/id/ --> perfil do médico
# www.volllmed.online/medico/id/alterar/ --> alterar cadastro do médico

# www.volllmed.online/medico/id/consultas/


# PACIENTE
# www.volllmed.online/paciente/id/ --> perfil do paciente
# www.volllmed.online/paciente/id/alterar/ --> alterar cadastro do paciente

# www.volllmed.online/paciente/id/consultas/cadastar/
# www.volllmed.online/paciente/id/consultas/id/ --> ver, alterar, deletar


# SECRETARIO
# www.volllmed.online/secretario/id/ --> perfil do secretario
# www.volllmed.online/secretario/id/alterar/ --> alterar cadastro do secretario

# www.volllmed.online/secretario/id/consultas/cadastar/
# www.volllmed.online/secretario/id/consultas/id/ --> ver, alterar, deletar


# CONSULTA
