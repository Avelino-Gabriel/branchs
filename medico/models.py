from django.db import models

# Create your models here.
class Especialidade(models.Model):
    id_especialidade = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=256)
    descricao = models.TextField()

    def __str__(self):
        return self.nome


class Medico(models.Model):
    id_medico = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=256)
    endereco = models.TextField()
    telefone = models.CharField(max_length=11)
    email = models.EmailField(max_length=254)
    data_nascimento = models.DateField(auto_created=False, auto_now=False, auto_now_add=False)
    crm = models.CharField(max_length=12)
    especialidade_id = models.OneToOneField(Especialidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome