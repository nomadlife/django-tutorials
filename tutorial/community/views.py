from django.shortcuts import render
from community.forms import *

# Create your views here.

def write(request):
	if request.method == 'PSOT':
		form = Form(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = Form()

	return render(request, 'write.html', {'form':form})
