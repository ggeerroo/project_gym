from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from sessions.models import Routine, Exercise, Session

""" class SessionDetail(DetailView):
    #todo


class SessionCreate(CreateView):
    #todo
 """



class RoutineList(ListView):
    model = Routine


class RoutineDetail(DetailView):
    model = Routine


class ExerciseDetail(DetailView):
    model = Exercise

""" 
class RoutineCreate(CreateView):
    #todo



class RoutineUpdate(UpdateView):
    #todo



class RoutineDelete(DeleteView):
    #todo






 """
