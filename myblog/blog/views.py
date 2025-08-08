from django.shortcuts import HttpResponse

# Create your views here.
def home_page(request):
    return HttpResponse("<h1>Hello world</h1>")