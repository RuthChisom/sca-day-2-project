from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def show_courses(request):
    return render(request, 'coursepage.html')