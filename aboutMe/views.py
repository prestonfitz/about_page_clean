from django.shortcuts import render

# Create your views here.
def indexPageView(request):
    return render(request, 'aboutMe/index.html')

def aboutPageView(request):
    return render(request, 'aboutMe/about.html')

def contactPageView(request):
    return render(request, 'aboutMe/contact.html')

def resumePageView(request):
    return render(request, 'aboutMe/resume.html')

def tableauPageView(request):
    return render(request, 'aboutMe/tableau.html')