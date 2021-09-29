from django.urls import path, include
from django.views.generic.list import ListView
from sessions.views import RoutineList, RoutineDetail, ExerciseDetail


app_name = 'sessions'

urlpatterns = [
    path('all_routines/', RoutineList.as_view(), name='routines'),
    path('routine/<int:pk>/', RoutineDetail.as_view(), name='routine_detail'),
    path('exercise/<int:pk>/', ExerciseDetail.as_view(), name='exercise_detail'),

]