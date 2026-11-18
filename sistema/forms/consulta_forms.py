from django import forms
from sistema.models import *

# Formulário da Consulta
class ConsultaForm(forms.ModelForm):

    class Meta:
        model = Consulta
        fields = ['paciente_id', 'medico_id', 'data_consulta', 'observacao', 'status',]
        # ativa não aparece: é preenchido automaticamente
        labels = {
            'paciente_id': 'ID do Paciente',
            'medico_id': 'ID do Médico',
            'data_consulta': 'Data da Consulta',
            'observacao': 'Observação',
            'status': 'Status',
        }