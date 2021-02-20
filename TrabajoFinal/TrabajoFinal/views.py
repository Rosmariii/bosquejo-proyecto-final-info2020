from django.shortcuts import render

def Principal(request):
    return render(request,'prueba.html')

def Segunda(request):
    return render(request,'segunda.html')
