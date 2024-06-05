from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    cpf = models.CharField(max_length=11)
    identidade = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Processo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    numero_processo = models.CharField(max_length=100)
    vara = models.CharField(max_length=100)
    local = models.CharField(max_length=100)

    def __str__(self):
        return self.numero_processo

class Atualizacao(models.Model):
    processo = models.ForeignKey(Processo, on_delete=models.CASCADE)
    informacoes = models.TextField()

    def __str__(self):
        return self.informacoes