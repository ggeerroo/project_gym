from django.db import models
from model_clone import CloneMixin
from django.core.validators import MinLengthValidator
from django.conf import settings
from datetime import timedelta
from django.urls import reverse



class Exercise(CloneMixin, models.Model):
    name = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2, "Name must be greater than 2 characters")]
    )
    sets = models.PositiveSmallIntegerField(default=1)
    repetitions = models.PositiveSmallIntegerField(default=1)
    weight = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('sessions:exercise_detail', kwargs={'pk': self.pk})

    # Shows up in the admin list
    def __str__(self):
        return self.name



class Routine(models.Model):
    name = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2, "Name must be greater than 2 characters")]
    )

    exercises = models.ManyToManyField(Exercise)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Session(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)
    
    """  start_time = models.DateTimeField(auto_now_add=True)
    finish_time = models.DateTimeField(auto_now_add=True) """
    duration = models.DurationField(null=True)
    
    def get_absolute_url(self):
        return reverse('sessions:session_detail', kwargs={'pk': self.pk})
   
    def __str__(self):
        return "Session of " + str(self.date)




