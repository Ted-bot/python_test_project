from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.student_id}) - {self.branch}"