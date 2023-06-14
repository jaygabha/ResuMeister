from django.shortcuts import render, redirect

# Create your views here.

import pymongo
from utils import client
from django.views import View


class HomePageView(View):
    def get(self, request):
        if request.session.has_key('username'):
            username=request.session['username']
            response = redirect('resumeister/homepage')
        else:
            response = redirect('resumeister/login', msg='Session Time Out. Please Login')
        return response


class LoginView(View):
    def get(self, request):
        response = render(request,'login.html')
        return response
    def post(self, request):
        if request.session.has_key('username'):
            return redirect('resumeister/homepage')

