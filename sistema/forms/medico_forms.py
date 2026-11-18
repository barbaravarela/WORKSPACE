from django import forms
from sistema.models import *

ESPECIALIDADES = [
    ('CARDIOLOGIA', 'Cardiologia'),
    ('DERMATOLOGIA', 'Dermatologia'),
    ('GINECOLOGIA', 'Ginecologia'),
    ('NEUROLOGIA', 'Neurologia'),
    ('OFTAMOLOGIA', 'Oftamologia'),
    ('ORTOPEDIA', 'Ortopedia'),
    ('PEDIATRIA', 'Pediatria'),
]

# Formulário de Médico (usado para cadastro e edição)
class MedicoForm(forms.ModelForm):
    # Troca o CharField padrão por um <select> com opções fixas
    especialidade = forms.CharField(
        choices=[('', 'Selecione uma especialidade')] + ESPECIALIDADES,
        label='Especialidade',
    )

    class Meta:
        model = Medico
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'crm', 'especialidade',]
        # criacao_data e ativo não aparecem: são preenchidos automaticamente
        labels = {
            'nome': 'Nome',
            'sobrenome': 'Sobrenome',
            'email': 'E-mail',
            'telefone': 'Telefone',
            'crm': 'CRM',
        }