from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def index(request):
	print()
	print('Index')

	#return HttpResponse('Hello World !')
	return render(request, 'pages/index.html')


def about(request):
	print()
	print('about')

	return render(request, 'pages/about.html')	