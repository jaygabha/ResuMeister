from django.urls import path
from . import views
from .views import HomePageView, LoginView, RegisterView

app_name = 'carapp'
urlpatterns = [
    path('', HomePageView.as_view(), name='Landing Page'),
    path('login', LoginView.as_view(), name='Login'),
    path('register', RegisterView.as_view(), name="Register")
]
