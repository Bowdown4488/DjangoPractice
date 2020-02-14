from django.http import HttpResponse
from django.shortcuts import render
from .forms import TestForm,RawFormTest
from .models import Test
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

def form_view (request):
    form = TestForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TestForm() 
    
    my_context = {  
        'form':form
    }
    return render(request, "form.html", my_context)

def raw_html_form_view (request):
    if request.method == "POST":
        title = request.POST
        print(title)

    my_context = {}
    return render(request, "raw_html_forms.html", my_context)

def raw_form_view (request):
    rawForm = RawFormTest()
    if request.method == "POST":
        rawForm = RawFormTest(request.POST)  #Validation erors (required field)
        if rawForm.is_valid():
            print(rawForm.cleaned_data) #validated data
            Test.objects.create(**rawForm.cleaned_data) #error but add ** to pass as argse
        else:
            print(rawForm.errors)
    context = {  
        'rawForm':rawForm
    }
    return render(request, "raw_form.html", context)

def get_data (request):
    forms = Test.objects.all() #search all
    context = {
        'forms': forms
    }
    return render(request, "get_data.html", context)

def get_data_one (request, id):
    forms = Test.objects.get(id=id) #search specific
    context = {
        'forms': forms
    }
    return render(request, "get_data_specific.html", context)  