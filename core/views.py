from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from core.models import Teacher,Student,Assignment,Material
from django.urls import reverse_lazy




# Create your views here.
class HomepageView(TemplateView):
    Template_name='home.html'


class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers/teacher_index.html'
    context_object_name = 'teachers'


class TeacherCreateView(CreateView):
    model = Teacher
    fields = ['full_name','email','phone_no','department','user', 'join_date']
    template_name = 'teachers/teacher_form.html'
    success_url = reverse_lazy('teacher.index')



class StudentListView(ListView):
    model = Student
    template_name = 'home.html'
    context_object_name = 'students'


class StudentCreateView(CreateView):
    model = Student
    fields = ['full_name','email','phone_no','user']
    template_name = 'students/student_form.html'
    success_url = 'student.index'

class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teachers/teacher_detailhtml'
    context_object_name = 'teacher'

class TeacherUpdateView(UpdateView):
    model = Teacher
    template_name = 'teachers/teacher_form.html'
    fields = ['full_name','email','join_date','phone_no','user']
    success_url = reverse_lazy('teacher.index')

class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'teachers/teacher_delete_confirm.html'
    context_object_name = 'teacher'
    success_url = reverse_lazy('teacher.index')
