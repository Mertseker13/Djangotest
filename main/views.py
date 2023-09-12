from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# def index(request):
#     return HttpResponse("<h1>Hello World<h1>")

def index(request):
    data = {'title':'Главная'}
    #               'test_list':['str',69,86.2,True],
    #               'person_object':{
    #                   'name': 'Вася',
    #                   'age': 23,
    #                   'hobby':'coding'}}

    return render(request, 'main/index.html',data)

def about(request):
    return render(request,"main/about.html")


# def about(request):
#     return HttpResponse("<h2>About<h2>")
