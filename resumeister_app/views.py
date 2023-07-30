from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
import pymongo
from utils import db
from django.urls import reverse
from urllib.parse import urlencode
from django.views import View
from .forms import UploadFileForm
import requests

class HomePageView(View):
    def get(self, request):
        if request.session.has_key('email'):
            return redirect('/main')
        return render(request, 'resumeister_app/home.html')


class LoginView(View):
    def get(self, request):
        msg = ''
        msg = request.GET.get('msg')
        response = render(request, 'resumeister_app/login.html', {"msg":msg})
        return response
    def post(self, request):
        if request.session.has_key('email'):
            return redirect('/main')
        else:
            email = request.POST.get("email")
            pwd = request.POST.get("pass")
            user = db["users"].find_one({"email": email})
            if user:
                if str(pwd) == str(user.get("password")):
                    request.session['email'] = email
                    request.session['first_name'] = user["first_name"]
                    request.session['last_name'] = user["last_name"]
                    return redirect('/main')
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
        if request.session.has_key('email'):
            return redirect('/main')
        msg = ''
        msg = request.GET.get('msg')
        response = render(request, 'resumeister_app/register.html', {"msg": msg})
        return response
    def post(self, request):
        if request.session.has_key('email'):
            return redirect('/main')
        else:
            email = request.POST.get("email")
            pwd = request.POST.get("pass")
            first_name = request.POST.get("firstName")
            last_name = request.POST.get("lastName")
            user = db["users"].find_one({"email": email})
            if user:
                base_url = reverse('resumeister_app:Login', )
                query_string = urlencode({'msg': "Account Already Exists. Please login"})
                url = '{}?{}'.format(base_url, query_string)
                return redirect(url)
            else:
                db['users'].insert_one({
                    "email": email,
                    "password": pwd,
                    "first_name": first_name,
                    "last_name": last_name
                })
                request.session['email'] = email
                request.session['first_name'] = first_name
                request.session['last_name'] = last_name
                return redirect('/main')


class Home(View):
    def get(self,request):
        # response = HttpResponse()
        # response.write("<p> Email: " + request.session.get("email") + "</p>")
        return render(request, 'resumeister_app/main.html')
    
# class Main(View):
#     def get(self,request):
#         if request.session.has_key('email'):
#             return redirect('/homepage_logged_in')
#         return render(request, 'resumeister_app/main.html')



class CreateResume(View):
    def get(self,request):
        # response = HttpResponse()
        # response.write("<p> Email: " + request.session.get("email") + "</p>")
        return render(request, 'resumeister_app/createResume.html')


def handle_uploaded_file(f, filename):
    with open(filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
class UploadResume(View):
    def get(self, request):
        form = UploadFileForm()
        return render(request, 'resumeister_app/uploadResume.html', {"form": form})

    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            name = str(request.FILES["file"].name)
            ext = name.split('.')[-1]
            filename = str('/Users/jayga/PycharmProjects/ResuMeister/ParsingApp/new_upload.' + ext)
            handle_uploaded_file(request.FILES["file"], filename)
            data = requests.get("http://127.0.0.1:5004/parse_resume", params={"file_path": filename}).json().get("parsed_resume")
            return render(request, 'resumeister_app/createResume.html', {"data": data} )
        else:
            raise FileNotFoundError
ç