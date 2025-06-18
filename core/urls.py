from django.urls import path
from core.views import HomepageView,TeacherListView,TeacherCreateView,StudentListView,StudentCreateView,TeacherDeleteView,TeacherDetailView,TeacherUpdateView

urlpatterns = [

    path('',HomepageView.as_view(),name='home'),
    path('teacher/list/',TeacherListView.as_view(),name = 'teacher.index'),
    path('teacher/create/',TeacherCreateView.as_view(),name = 'teacher.create'),
    path('student/list/',StudentCreateView.as_view(),name = 'student.index'),
    path('student/create/',StudentCreateView.as_view(),name = 'student.create'),
    path('teacher/<int:pk>/detail/',TeacherDetailView.as_view(),name = 'teacher.detail'),
    path('teacher/<int:pk>/edit/',TeacherUpdateView.as_view(),name = 'teacher.edit'),
    path('teacher/<int:pk>/delete/',TeacherDeleteView.as_view(),name = 'teacher.delete'),
]