from django.urls import path

from app.views.timetable import TimeTableAPIList, TimeTableAPICreate, TimeTableAPIUpdate, \
    TimeTableAPIRetrieveDestroy, GroupAPIList, DayAPIList, TeacherAPIList, UserGroupUpdate

urlpatterns = [
    path('', TimeTableAPIList.as_view()),
    path('create/', TimeTableAPICreate.as_view()),
    path('update/<int:pk>/', TimeTableAPIUpdate.as_view()),
    path('detail_delete/<int:pk>/', TimeTableAPIRetrieveDestroy.as_view()),
    path('day/<int:pk>/', DayAPIList.as_view()),
    path('group/', GroupAPIList.as_view()),
    path('teacher/<int:pk>', TeacherAPIList.as_view()),
    path('group_update/<int:pk>', UserGroupUpdate.as_view()),
]
