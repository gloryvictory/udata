from django.shortcuts import render

# Create your views here.

def index(request):#создаем свою функцию
    context = {}#с помощью словаря можем передать модель и форму в шаблон HTML
    return render(request, 'dataview/index.html', context)#собственно вызываем шаблон HTML