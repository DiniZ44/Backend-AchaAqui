from django.contrib import admin

# Register your models here.
from core.models import Contato, Endereco, Empresa, Usuario, Favorito, Categoria, SubCategoria, Feedback, Servico

admin.site.register(Contato)
admin.site.register(Endereco)
admin.site.register(Categoria)
admin.site.register(SubCategoria)
admin.site.register(Favorito)
admin.site.register(Feedback)
admin.site.register(Servico)
admin.site.register(Empresa)
admin.site.register(Usuario)