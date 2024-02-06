from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
global pages
pages = ["Главная", "Книги", "Фильмы", "Игры", "Энциклопедия", "Магазин", "Контакты"]

def main(request):
    data = {'pages': pages}
    return render(request, template_name='HP_World/main.html', context=data)

def foundation(request, page):
    data = {'pages': pages, 'page':page}
    print(page)
    return render(request, template_name='HP_World/foundation.html', context=data)

def elements(request, section):
    data = {'pages': pages, 'section':section}
    return render(request, template_name='HP_World/main.html', context=data)

def info(request, id):
    data = {'pages': pages, 'id':id}
    return render(request, template_name='HP_World/main.html', context=data)

def grimoire(request):
    return HttpResponse('Grimoire')

def shop(request):
    return HttpResponse('Shop')