from django.shortcuts import render

def home(request):
    return render(request, 'gaming/home.html')

def games(request):
    return render(request, 'gaming/games.html')

def about(request):
    return render(request, 'gaming/about.html')