from django.urls import path
from welcome.views import SignUpView
from django.conf.urls.static import static
from django.conf import settings


app_name = 'welcome'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]