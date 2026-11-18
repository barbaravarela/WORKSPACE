from django import forms
from sistema.models import *

# Formulário de Paciente (usado para cadastro e edição)
class PacienteForm(forms.ModelForm):

    "No model Paciente o CPF tem 11 char, mas aqui podemos aceitar até 14 por causa do . e -"
    cpf = forms.CharField(
        max_length=14,
        label="CPF"
    )

    class Meta:
        model = Paciente
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'cpf',]
        # criacao_data e ativo não aparecem: são preenchidos automaticamente
        # mensagem não aparece: vai ser usada só para a edição, não para o cadastro
        labels = {
            'nome': 'Nome',
            'sobrenome': 'Sobrenome',
            'email': 'E-mail',
            'telefone': 'Telefone',
            'cpf': 'CPF',
        }