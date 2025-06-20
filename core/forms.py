from django import forms
from core.models import Teacher, Student, Assignment

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['full_name', 'email', 'department', 'phone_no', 'join_date', 'user']
        widgets = {
            'join_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        } 

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title','question','question_file' ,'start_date', 'end_date', 'full_mark','remark','teacher', 'subject']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }   