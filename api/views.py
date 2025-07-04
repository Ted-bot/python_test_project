from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def studentsView(request):
    student_view_data = {
        "students": [
            {"name": "Alice", "age": 20},
            {"name": "Bob", "age": 22},
        ]}
    return JsonResponse(student_view_data)