from django.urls import path, include
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from sessions.views import RoutineList, RoutineDetail, ExerciseDetail, SessionCreate, SessionDetail, SessionDelete, ExerciseUpdate, RoutineUpdate
from django.conf.urls.static import static
from django.conf import settings


app_name = 'sessions'

urlpatterns = [
    path('all_routines/', RoutineList.as_view(), name='routine_list'),
    path('routine/<int:pk>/', RoutineDetail.as_view(), name='routine_detail'),
    path('routine/<int:pk>/update', RoutineUpdate.as_view(), name='routine_update'),
    path('exercise/<int:pk>/update/', ExerciseUpdate.as_view(), name='exercise_update'),
    path('exercise/<int:pk>/detail/', ExerciseDetail.as_view(), name='exercise_detail'),
    path('new/', SessionCreate.as_view(), name='session_create'),
    path('detail/<int:pk>/', SessionDetail.as_view(), name='session_detail'),
    path('delete/<int:pk>', SessionDelete.as_view(), name='session_delete'),
    path('progress', TemplateView.as_view(template_name='sesh/progress_charts.html'), name='progress'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




