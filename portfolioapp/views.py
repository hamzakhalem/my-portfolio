from django.shortcuts import render

# Create your views here.
def  home(request):
    return render (request, 'index.html')
def  homefr(request):
    return render (request, 'indexfr.html')
def  homear(request):
    return render (request, 'indexar.html')