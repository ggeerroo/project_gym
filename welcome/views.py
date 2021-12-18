from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


# Create new user subclassing the generic CreateView class and using Django's UserCreationForm
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    """ def post(self, request, *args, **kwargs):
        
        return  """