from django.urls import path
from . import views
from .views import HomePageView

app_name = 'carapp'
urlpatterns = [
    path('', HomePageView.as_view, name='Landing Page'),
]
