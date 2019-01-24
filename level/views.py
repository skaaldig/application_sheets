from django.shortcuts import render

# Create your views here.

def level_page(request):
	return render(request, 'pages/level_form.html')