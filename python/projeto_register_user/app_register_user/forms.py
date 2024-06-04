# forms.py
from django import forms
from .models import Cliente, Processo, Atualizacao

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone', 'cpf', 'identidade']

class ProcessoForm(forms.ModelForm):
    class Meta:
        model = Processo
        fields = ['numero_processo', 'vara', 'local']

class AtualizacaoForm(forms.ModelForm):
    class Meta:
        model = Atualizacao
        fields = ['informacoes']