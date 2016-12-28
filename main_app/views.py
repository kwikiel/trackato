from django.shortcuts import render

def index(request):
		name = 'Usecase metric'
		value = 1337
		context = {'treasure_name': name,
						'treasure_val': value}
		return render(request, 'index.html', context)
