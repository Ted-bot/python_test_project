from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def students(request):
    students_list = ["Alice", "Bob", "Charlie"]
    return HttpResponse(students_list)