from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    # return HttpResponse('Hello World') - this only renders a string
    #this renders a whole html page
    return render(request, 'home.html', {'name':'Ruth'})