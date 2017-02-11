#!-*- conding: utf8 -*-
from django.contrib import admin
from cliente.models import Cliente



class ClienteAdmin(admin.ModelAdmin):
	model = Cliente
	date_hierarchy = 'data_nascimento'#cria uma hieraquia de tempo, linha do tempo, consulta por data
	#fields = ('nome', 'data_nascimento') #mostra só os campos indicado
	#exclude = ('data_nascimento',)#mostra tudo, menos o campo setado
	list_display = ('nome', 'data_nascimento', 'salario', 'email', 'filhos' )#cria barras na colunas ordenaveis
	list_filter = ('nome', 'data_nascimento', 'salario', 'email', 'filhos' )#cria menu de filtro ordenado
	#readonly_fields = ('filhos',)#Deixa o campo setado somente leitura, não pode ser editado
	search_fields = ('nome', 'data_nascimento', 'salario', 'email', 'filhos' )#cria barra de pequisa em cima da tabelas  



admin.site.register(Cliente, ClienteAdmin)

