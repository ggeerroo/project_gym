from django.urls import path, include
from django.views.generic.list import ListView
from sessions.views import RoutineList


app_name = 'sessions'

urlpatterns = [
    path('routines/', RoutineList.as_view(), name='routines'),
    path('routines/<int:pk>/', RoutineDetail.as_view(), name='routines_detail'),

]