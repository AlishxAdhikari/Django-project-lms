from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView,CreateView
from core.models import Teacher,Student,Assignment,Material



# Create your views here.
class HomepageView(TemplateView):
    Template_name='home.html'


class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers/teacher_index.html'
    context_object_name = 'teachers'


class TeacherCreateView(CreateView):
    model = Teacher
    fields=['full_name','email','phone_no','department','user']
    template_name = 'teachers/teacher_form.html'
    success_url = 'teacher_index'



class StudentListView(ListView):
    model = Student
    template_name = 'home.html'
    context_object_name = 'students'


class StudentCreateView(CreateView):
    model = Teacher
    fields=['full_name','email','phone_no','department','user']
    template_name = 'teachers/teacher_form.html'
    success_url = 'teacher_index'



