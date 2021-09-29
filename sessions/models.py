from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings
from datetime import timedelta



class Exercise(models.Model):
    name = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2, "Name must be greater than 2 characters")]
    )
    sets = models.PositiveIntegerField(
        validators=[MinLengthValidator(1, "Number of sets must be at least 1.")]
    )
    repetitions = models.PositiveIntegerField(
        validators=[MinLengthValidator(1, "Number of repetiions must be at least 1.")]
    )
    weight = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
    
    # I need to enter a timedelta type for the duration (finishing_time - starting_time)
    duration = models.DurationField()


    def __str__(self):
        return "Session of " + self.date 