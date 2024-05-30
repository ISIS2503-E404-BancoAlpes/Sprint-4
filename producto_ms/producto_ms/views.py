from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def index_prod(request):
    return render(request,'index.html')
