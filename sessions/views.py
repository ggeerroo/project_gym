from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from sessions.models import Routine, Exercise, Session
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from datetime import timedelta



class SessionCreate(LoginRequiredMixin, CreateView):
    model = Session
    fields = ['routine']
    
    # This method is called when valid form data has been POSTed.
    # It should return an HttpResponse.
    def form_valid(self, form):  
        session = form.save(commit=False)  # Returns an object that hasn't been saved yet
        session.user = self.request.user
        session.save()
        return super().form_valid(form)
        
        



class SessionDetail(LoginRequiredMixin, DetailView):
    model = Session

    # Save the duration of the session in the db
    def post(self, request, *args, **kwargs):
        session = self.get_object()      
        #   Get the string duration from the POST request, turn it into an int, 
        #   divide by 1000 to get the amount of seconds, format it w/ timedelta and update session
        seconds = int(request.POST['duration']) / 1000
        session.duration = timedelta(seconds = int(seconds)) 
        session.save()
        return HttpResponseRedirect(reverse_lazy('sessions:session_detail', args=[session.id]))


class RoutineList(LoginRequiredMixin, ListView):
    model = Routine


class RoutineDetail(LoginRequiredMixin, DetailView):
    model = Routine


class ExerciseDetail(LoginRequiredMixin,DetailView):
    model = Exercise



class SessionExerciseUpdate(LoginRequiredMixin, UpdateView):


    def post(self, request, *args, **kwargs):
        new_exercise = Exercise(
            

        )


""" 
class RoutineCreate(CreateView):
    #todo



class RoutineUpdate(UpdateView):
    #todo



class RoutineDelete(DeleteView):
    #todo






 """
