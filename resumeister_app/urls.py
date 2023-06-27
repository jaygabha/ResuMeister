from django.urls import path
from . import views
from .views import HomePageView, LoginView, RegisterView, Home

app_name = 'resumeister_app'
urlpatterns = [
    path('', HomePageView.as_view(), name='Landing Page'),
    path('login', LoginView.as_view(), name='Login'),
    path('register', RegisterView.as_view(), name="Register"),
    path('main', Home.as_view(), name="Homepage Logged In"),
    
]
