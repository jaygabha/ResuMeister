from django.urls import path
from . import views
from .views import HomePageView, LoginView, RegisterView, Home, CreateResume, UploadResume, SaveResume, ResumeCreation

app_name = 'resumeister_app'
urlpatterns = [
    path('', HomePageView.as_view(), name='Landing Page'),
    path('login/', LoginView.as_view(), name='Login'),
    path('logout/', views.Logout, name='Logout'),
    path('register/', RegisterView.as_view(), name="Register"),
    path('main/', Home.as_view(), name="Homepage Logged In"),
    path('createResume/<str:resume>', views.CreateResume, name="Create Resume"),
    path('deleteResume/<str:resume>', views.DeleteResume, name="Create Resume"),
    path('uploadResume/<str:title>', views.UploadResume, name="Upload Resume"),
    path('saveResume/', SaveResume.as_view(),name="Save Resume"),
    path('create/', ResumeCreation.as_view(), name="ResumeCreatiom")
]
