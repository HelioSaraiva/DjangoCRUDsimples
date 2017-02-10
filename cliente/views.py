from django.shortcuts import render, redirect
from django.http import HttpResponse
from cliente.models import Cliente
from cliente.form import ClienteForm



def home(request):
	return HttpResponse('Hello word')


def cliente(request):
	data = {}
	data['lista_clientes'] = Cliente.objects.all()
	data['djangomoc'] = 'Primerio CRUD simples criado no Django'
	return render(request,'cliente.html', data)


def cliente_update(request, pk):
	cliente = Cliente.objects.get(pk=pk)

	form = ClienteForm(request.POST or None, instance=cliente)
	if form.is_valid():
		form.save()
		return redirect('cliente_principal')
	return render(request, 'cliente_detalhe.html', {'object':cliente, 'form':form})


def create(request):
	form = ClienteForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect('cliente_principal')
	
	return render(request, 'cliente_novo.html', {'form':form})	

def delete(request, pk):
	cliente = Cliente.objects.get(pk=pk)

	if request.method == 'POST':
		
		cliente.delete()
		return redirect('cliente_principal')
	return render(request, 'cliente_delete_confirm.html', {'object': cliente})
	






