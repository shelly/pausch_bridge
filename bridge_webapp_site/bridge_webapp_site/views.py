from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import TextForm

def index(request):
	return render(request, 'index.html')

def submit_form_text(request):

	if request.method == 'POST':
		form = TextForm(request.POST)

		if form.is_valid(): 
			form.submit_text()
		
		return HttpResponseRedirect('/')

	else:
		form = TextForm()

	return render(request, 'index.html', {'form':form})