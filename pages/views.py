from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello World</h1>") #String of html
    return render(request, "home.html", {})

def next_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Other page</h1>") 
    # context for passing
    my_context = {  
        "text": "test text",
        "number": 123,
        "list": [1,2,3]
    }
    return render(request, "next.html", my_context)
