from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from sessions.models import Routine, Exercise, Session
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from datetime import timedelta, datetime



class SessionCreate(LoginRequiredMixin, CreateView):
    model = Session
    fields = ['routine']
    """ template = 'sesh/routine_select.html' """
    template_name_suffix = '_create_form'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['routines'] = Routine.objects.all()
        return context

    # This method is called when valid form data has been POSTed.
    # It should return an HttpResponse.
    def form_valid(self, form):  
        session = form.save(commit=False)  # Returns an object that hasn't been saved yet
        session.user = self.request.user
        session.save()
        return super().form_valid(form)
        
        



class SessionDetail(LoginRequiredMixin, DetailView):
    model = Session


    # We get the session's number, because it's not necessarily the same as its id (cancelled sessions, etc.)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['session_number'] = Session.objects.all().count()
        return context

    # Save the duration of the session and last workout for the routine in the db 
    def post(self, request, *args, **kwargs):
        session = self.get_object()      
        #   Get the string duration from the POST request, turn it into an int, 
        #   divide by 1000 to get the amount of seconds, format it w/ timedelta and update session
        seconds = int(request.POST['duration']) / 1000
        session.duration = timedelta(seconds = int(seconds)) 
        session.save()

        # Save date of last workout using this routine
        routine = Routine.objects.get(name=session.routine)
        routine.last_workout = datetime.now()
        routine.save()

        return HttpResponseRedirect(reverse_lazy('sessions:session_detail', args=[session.id]))



class SessionDelete(LoginRequiredMixin, DeleteView):
    model = Session
    success_url = '/'



class RoutineList(LoginRequiredMixin, ListView):
    model = Routine


class RoutineDetail(LoginRequiredMixin, DetailView):
    model = Routine


class RoutineUpdate(LoginRequiredMixin, UpdateView):
    model = Routine
    fields = ['name', 'exercises']    


class ExerciseDetail(LoginRequiredMixin,DetailView):
    model = Exercise      
   

class ExerciseUpdate(LoginRequiredMixin, UpdateView):
    model = Exercise
    fields = ['sets', 'repetitions', 'weight']

    #   Create a clone of the exercise so we can keep a record of the progress
    def form_valid(self, form):
        exercise = self.get_object()
        exercise_clone = exercise.make_clone()
        exercise_clone.updated_at = datetime.now()
        exercise_clone.save()
        return super().form_valid(form) 



""" class NotesUpdate(LoginRequiredMixin, UpdateView):
    def form_valid(self, form):
        exercise = self.get_object()
        exercise_clone = exercise.make_clone()
        exercise_clone.updated_at = datetime.now()
        exercise_clone.save()
        return super().form_valid(form)  """

""" 
class RoutineCreate(CreateView):
    #todo







class RoutineDelete(DeleteView):
    #todo






 """
