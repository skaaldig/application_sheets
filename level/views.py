from django.shortcuts import render

# Create your views here.

def level_general(request):
	return render(request, 'pages/level_form.html')


def level_tank(request):
	return render(request, 'pages/level_tank_material.html')