from django.shortcuts import render
from .models import Student  # make sure this is correct

def student_list(request):
    students = Student.objects.all()  # fetch all students
    return render(request, 'library/student_list.html', {'students': students})
