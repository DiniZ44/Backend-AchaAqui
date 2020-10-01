from django.db import models


class Contato(models.Model):
    telefone = models.IntegerField()


class Feedback(models.Model):
    classificao = models.IntegerField()
    descricao = models.CharField


class Endereco(models.Model):
    rua = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    cep = models.IntegerField()
    numero = models.IntegerField()


class Categoria(models.Model):
    descricao = models.CharField(max_length=50)


class SubCategoria(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete= models.PROTECT)
    descricao = models.CharField(max_length=50)

class Servico(models.Model):
    descricao = models.CharField(max_length=50)
    subCategoria = models.ForeignKey(SubCategoria, on_delete= models.PROTECT)

class Favorito(models.Model):
    servico = models.ForeignKey(Servico, on_delete= models.PROTECT)

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=20)
    senha = models.CharField(max_length=10)
    contato = models.ForeignKey(Contato, on_delete= models.PROTECT)
    favorito = models.ForeignKey(Favorito, on_delete= models.PROTECT)

class Empresa(models.Model):
    #imagem = models.ImageField()
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)
    horario = models.CharField(max_length=50)
    palavrasChaves = models.CharField(max_length=50)
    feedback = models.ForeignKey(Feedback, on_delete= models.PROTECT)
    contato = models.ForeignKey(Contato, on_delete= models.PROTECT)
    endereco = models.ForeignKey(Endereco, on_delete= models.PROTECT)
    servico = models.ForeignKey(Servico, on_delete= models.PROTECT)



