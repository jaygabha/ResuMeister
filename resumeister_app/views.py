from django.shortcuts import render, redirect

# Create your views here.

import pymongo
from utils import client
from django.views import View


class HomePageView(View):
    def get(self, request):
        if request.session.has_key('username'):
            username=request.session['username']
            return redirect('homepage_logged_in')
        return render(request, 'resumeister_app/home.html')


class LoginView(View):
    def get(self, request):
        response = render(request, 'resumeister_app/login.html')
        return response
    def post(self, request):
        if request.session.has_key('username'):
            return redirect('homepage_logged_in')

class RegisterView(View):
    def get(self, request):
        response = render(request, 'resumeister_app/register.html')
        return response
    def post(self, request):
        if request.session.has_key('username'):
            return redirect('homepage_logged_in')