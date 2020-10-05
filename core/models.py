from django.db import models


class Contato(models.Model):
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.telefone

class Feedback(models.Model):
    classificao = models.IntegerField()
    descricao = models.TextField(default='')

    def __str__(self):
        return 'Classificação', self.classificao, 'Feed -' + self.descricao

class Endereco(models.Model):
    rua = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=15)
    numero = models.IntegerField()

    def __str__(self):
        return 'Rua - '+ self.rua + ' - Bairro - ' +self.bairro +' Cidade - '+ self.cidade

class Categoria(models.Model):
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao


class SubCategoria(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete= models.PROTECT)
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao

class Servico(models.Model):
    descricao = models.CharField(max_length=50)
    subCategoria = models.ForeignKey(SubCategoria, on_delete= models.PROTECT)

    def __str__(self):
        return self.descricao

class Favorito(models.Model):
    servico = models.ForeignKey(Servico, on_delete= models.PROTECT)

    def __str__(self):
        return self.servico.descricao

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    senha = models.CharField(max_length=10)
    contato = models.ForeignKey(Contato, on_delete= models.PROTECT)
    favorito = models.ForeignKey(Favorito, on_delete= models.PROTECT)

    def __str__(self):
        return self.nome

class Empresa(models.Model):
    #imagem = models.ImageField()
    nome = models.CharField(max_length=50)
    descricao = models.TextField(default='')
    senha = models.CharField(max_length=50)
    horario = models.CharField(max_length=50)
    palavrasChaves = models.CharField(max_length=50)
    feedback = models.ForeignKey(Feedback, on_delete= models.PROTECT)
    contato = models.ForeignKey(Contato, on_delete= models.PROTECT)
    endereco = models.ForeignKey(Endereco, on_delete= models.PROTECT)
    servico = models.ForeignKey(Servico, on_delete= models.PROTECT)

    def __str__(self):
        return '%s %s %s' %(self.nome, self.descricao, self.servico.descricao)