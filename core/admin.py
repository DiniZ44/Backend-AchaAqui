from django.contrib import admin

# Register your models here.
from core.models import Contato, Endereco, Empresa, Usuario, Favorito, Categoria, SubCategoria, Feedback, Servico

class EmpresaAdmin (admin.ModelAdmin):
    list_display = (
        'nome', 'descricao', 'horario', 'premium', 'servico', 'contato'
    )

class EnderecoAdmin (admin.ModelAdmin):
    list_display = (
        'rua', 'bairro' ,'cidade','numero','uf', 'cep'
    )
class UsuarioAdmin(admin.ModelAdmin):
    list_display = (
        'nome', 'email', 'senha', 'contato'
    )
class FeedAdmin (admin.ModelAdmin):
    list_display = (
        'classificacao', 'descricao'
    )

admin.site.register(Categoria)
admin.site.register(SubCategoria)
admin.site.register(Servico)
admin.site.register(Feedback, FeedAdmin)
admin.site.register(Favorito)
admin.site.register(Contato)
admin.site.register(Endereco, EnderecoAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Empresa, EmpresaAdmin)

