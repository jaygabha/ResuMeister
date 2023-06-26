from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
import pymongo
from utils import db
from django.urls import reverse
from urllib.parse import urlencode
from django.views import View


class HomePageView(View):
    def get(self, request):
        if request.session.has_key('email'):
            return redirect('/homepage_logged_in')
        return render(request, 'resumeister_app/home.html')


class LoginView(View):
    def get(self, request):
        msg = ''
        msg = request.GET.get('msg')
        response = render(request, 'resumeister_app/login.html', {"msg":msg})
        return response
    def post(self, request):
        if request.session.has_key('email'):
            return redirect('/homepage_logged_in')
        else:
            email = request.POST.get("email")
            pwd = request.POST.get("pass")
            user = db["users"].find_one({"email": email})
            if user:
                if str(pwd) == str(user.get("password")):
                    request.session['email'] = email
                    request.session['first_name'] = user["first_name"]
                    request.session['last_name'] = user["last_name"]
                    return redirect('/homepage_logged_in')
                else:
                    base_url = reverse('resumeister_app:Login',)
                    query_string = urlencode({'msg': "Incorrect Password. Please try again"})
                    url = '{}?{}'.format(base_url, query_string)
                    return redirect(url)
            base_url = reverse('resumeister_app:Register', )
            query_string = urlencode({'msg': "No account found with that email. Please Register"})
            url = '{}?{}'.format(base_url, query_string)
            return redirect(url)



class RegisterView(View):
    def get(self, request):
        response = render(request, 'resumeister_app/register.html')
        return response
    def post(self, request):
        if request.session.has_key('email'):
            return redirect('/homepage_logged_in')

class Home(View):
    def get(self,request):
        response = HttpResponse()
        response.write("<p> Email: " + request.session.get("email") + "</p>")
        return response