from django.contrib import admin
from .models import Categoria
from .models import Erros

#Melhorar isso futuramente

def status_producao(modeladmin, request, queryset):
    queryset.update(categoria='1')
status_producao.short_description = "Marcar para Produção"

def status_homologacao(modeladmin, request, queryset):
    queryset.update(categoria='2')
status_homologacao.short_description = "Marcar para Homologação"

def status_desenvolvimento(modeladmin, request, queryset):
    queryset.update(categoria='3')
status_desenvolvimento.short_description = "Marcar para Desenvolvimento"

def status_arquivar(modeladmin, request, queryset):
    queryset.update(arquivar='True')
status_arquivar.short_description = "Arquivar erros selecionados"


class ErrosAdmin(admin.ModelAdmin):

    list_display = ['level', 'eventos', 'descricao', 'arquivar', 'categoria']
    #search_fields = ['level', 'categoria', 'eventos']
    list_filter = ['eventos', 'categoria', 'level']
    actions = [status_producao, status_homologacao, status_desenvolvimento, status_arquivar]

class CategoriaAdmin(admin.ModelAdmin):

    list_display = ['status', 'descricao']
    #search_fields = ['level', 'categoria', 'eventos']
    #list_filter = ['eventos', 'categoria', 'level']


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Erros, ErrosAdmin)

