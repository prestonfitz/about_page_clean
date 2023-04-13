from django.shortcuts import render

# Create your views here.
def indexPageView(request):
    return render(request, 'pokemon/index.html')

def authorPageView(request):
    return render(request, 'pokemon/Author.html')

def ballsPageView(request):
    return render(request, 'pokemon/balls.html')

def startersPageView(request):
    return render(request, 'pokemon/Starters.html')

def typesPageView(request):
    return render(request, 'pokemon/types.html')
