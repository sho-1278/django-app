from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from resf.forms import *
# Create your views here.

def index(request):
	form = UserQueryForm(request.POST or None)
	if request.method=="POST":
		form.save()
		#form = UserQueryForm()
		return redirect(reverse('thank_you_page'))
	context = {
	'form': form
	}
	return render(request,'resf/index.html', context)

def greet(request):
	return render(request, 'resf/greet.html')