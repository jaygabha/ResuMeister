from django.urls import path
from .views import HomePageView, LoginView, RegisterView, Home, CreateResume, UploadResume

app_name = 'resumeister_app'
urlpatterns = [
    path('', HomePageView.as_view(), name='Landing Page'),
    path('login/', LoginView.as_view(), name='Login'),
    path('register/', RegisterView.as_view(), name="Register"),
    path('main/', Home.as_view(), name="Homepage Logged In"),
    path('createResume/',CreateResume.as_view(), name="Create Resume"),
    path('uploadResume/', UploadResume.as_view(), name="Upload Resume"),
]
