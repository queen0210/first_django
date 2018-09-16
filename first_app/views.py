from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader


def first_view(request):
    print("this is my first django")
    return HttpResponse("this is django server")

def first_view2(request):
    print("this is templates view")
    return render(request,'html129.html')
def first_view3(request):
    print('this is templates view2')
    print('123')
    temp = loader.get_template('html129.html')
    content = temp.render(request = request)
    return HttpResponse(content)
def first_view4(request):
    print('this is templates view 4')
    print('hahaha')
    return render(request,'html129.html',context={"name":"maxintang","age":20})

