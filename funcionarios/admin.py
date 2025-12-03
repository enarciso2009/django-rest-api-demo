from django.contrib import admin
from .models import Funcionario

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'cargo', 'ativo')
    search_fields = ('nome', 'email', 'cargo')
    list_filter = ('ativo',)
    

