from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

list1=[
    {"id":1,"name":"class_python"},
    {"id":2,"name":"class_html"},
    {"id":3,"name":"class_jango"},
    {"id":4,"name":"class_c#"}
]
def detail(request):
    context={'list':list1}
    return render(request , 'app1/list.html' , context=context)

def detail2(request):
    context={'list':list1}
    return render(request , 'app1/list2.html',context=context )