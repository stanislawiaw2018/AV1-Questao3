from django.contrib import admin
from aplicacoes.models import *
# default: "Administração do Django"
admin.site.site_header = 'Painel de Controle'
# default: "Administração do Site"
admin.site.index_title = 'Aplicações'
# default: ”Site de administração do Django"
admin.site.site_title = 'Agendamento de Festas'

class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'nome','descricao'
    )

class TemaAdmin(admin.ModelAdmin):
    list_display = (
        'nome','valor'
    )

class AluguelAdmin(admin.ModelAdmin):
    list_display = (
        'tema','data_festa','horai','horat','valor','cliente'
    )

class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'nome','telefone'
    )

admin.site.register(Item,ItemAdmin)
admin.site.register(Endereco)
admin.site.register(Tema,TemaAdmin)
admin.site.register(Aluguel,AluguelAdmin)
admin.site.register(Cliente,ClienteAdmin)


