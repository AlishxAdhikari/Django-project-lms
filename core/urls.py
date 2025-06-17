from django.urls import path
from core.views import HomepageView,TeacherListView,TeacherCreateView

urlpatterns = [

    path('',HomepageView.as_view(),name='home'),
    path('teacher/list/',TeacherListView.as_view(),name = 'teacher.index'),
    path('teacher/list/',TeacherCreateView.as_view(),name = 'teacher.create'),
]