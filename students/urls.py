from django.urls import path
from . import views

urlpatterns = [
    # Define your URL patterns here
    # Example:
    # path('students/', StudentListView.as_view(), name='student-list'),
    path('', views.students),
]