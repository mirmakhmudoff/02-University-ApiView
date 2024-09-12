from django.urls import path
from .views import (
    FacultyList, FacultyDetail, GroupList, GroupDetail,
    KafedraList, KafedraDetail, SubjectList, SubjectDetail,
    TeacherList, TeacherDetail, StudentList, StudentDetail
)

urlpatterns = [
    path('faculties/', FacultyList.as_view(), name='faculty-list'),
    path('faculties/<int:pk>/', FacultyDetail.as_view(), name='faculty-detail'),
    path('groups/', GroupList.as_view(), name='group-list'),
    path('groups/<int:pk>/', GroupDetail.as_view(), name='group-detail'),
    path('kafedras/', KafedraList.as_view(), name='kafedra-list'),
    path('kafedras/<int:pk>/', KafedraDetail.as_view(), name='kafedra-detail'),
    path('subjects/', SubjectList.as_view(), name='subject-list'),
    path('subjects/<int:pk>/', SubjectDetail.as_view(), name='subject-detail'),
    path('teachers/', TeacherList.as_view(), name='teacher-list'),
    path('teachers/<int:pk>/', TeacherDetail.as_view(), name='teacher-detail'),
    path('students/', StudentList.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentDetail.as_view(), name='student-detail'),
]
