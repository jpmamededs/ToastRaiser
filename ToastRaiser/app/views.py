from django.shortcuts import render

# Create your views here.
def paginaprincipal(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def download(request):
    return render(request, 'download.html')

def contact(request):
    return render(request, 'contact.html')

def progress(request):
    return render(request, 'progress.html')


