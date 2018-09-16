from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def view_test1(request):
    print('this is view test1')
    return HttpResponse('view test1')
def view_test2(request):
    print('this is view test2')
    return HttpResponse('view test2~~~')
def view_test3(request):
    print('this is view test3')
    return HttpResponse('view text3~~~')

def view_vip1(request):
    print('this is view vip1')
    return HttpResponse('view vip1')
def view_vip2(request):
    print('this is view vip2')
    return HttpResponse('view vip2~~~')
def view_vip3(request):
    print('this is view vip3')
    return HttpResponse('view vip3~~~')
def goto_page(request):
    print('this is go to view page')
    return render(request,'view.html')
#a链接传值取值
def argument(request):
    id = request.GET.get("id")
    name = request.GET.get("name")
    geneder = request.GET.get("geneder")
    hobby = request.GET.getlist("hobby")
    print("id:",id,' name:',name,geneder,hobby)
    return HttpResponse('用户'+id)


