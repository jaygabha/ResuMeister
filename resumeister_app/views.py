import json

from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
import pymongo
import os
from utils import db
from django.urls import reverse
from urllib.parse import urlencode
from django.views import View
from .forms import UploadFileForm
import requests
from datetime import datetime
from .latex_converter import format_to_tex, save_to_tex, convert_latex_to_pdf
from bson import json_util


import spacy
from spacy.matcher import PhraseMatcher
from skillNer.general_params import SKILL_DB
from skillNer.skill_extractor_class import SkillExtractor
import en_core_web_sm

class HomePageView(View):
    def get(self, request):
        if request.session.has_key('email'):
            return redirect('/main')
        return render(request, 'resumeister_app/home.html')


class LoginView(View):
    def get(self, request):
        if request.session.has_key('email'):
            return redirect("resumeister_app:Homepage Logged In")
        msg = ''
        msg = request.GET.get('msg')
        response = render(request, 'resumeister_app/login.html', {"msg":msg})
        return response
    def post(self, request):
        if request.session.has_key('email'):
            return redirect("resumeister_app:Homepage Logged In")

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
            return redirect("resumeister_app:Homepage Logged In")
        msg = ''
        msg = request.GET.get('msg')
        response = render(request, 'resumeister_app/register.html', {"msg": msg})
        return response
    def post(self, request):
        if request.session.has_key('email'):
            return redirect("resumeister_app:Homepage Logged In")
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
                return redirect("resumeister_app:Homepage Logged In")


class Home(View):
    def get(self,request):
        if request.session.has_key('email'):
            resumes = list(db["resumes"].find({"email": request.session.get("email")}))
            resume_list = []
            for items in resumes:
                resume_list.append(items.get('title'))
            response = render(request, 'resumeister_app/main.html', {"resume": resumes, "resume_list": resume_list})
            response.set_cookie(key="parse_data", value="", expires=datetime.now())
            response.set_cookie(key="title", value="", expires=datetime.now())
            response.set_cookie(key="extract_data", value="", expires=datetime.now())
            return response
        else:
            return redirect("resumeister_app:Login")


class ResumeCreation(View):
    def get(self, request):
        if request.session.has_key('email'):
            response = render(request, "resumeister_app/resumecreation.html")
            response.set_cookie(key="extract_data", value="", expires=datetime.now())
            response.set_cookie(key="parse_data", value="", expires=datetime.now())
            response.set_cookie(key="title", value="", expires=datetime.now())
            return response
        else:
            return redirect("resumeister_app:Login")
    def post(self, request):
        if request.session.has_key('email'):
            title = request.POST.get("title")
            email = request.session.get("email")
            find_resume = list(db["resumes"].find({"email": email, "title": title}))
            print(find_resume)
            if len(find_resume)>0:
                return render(request, "resumeister_app/resumecreation.html", {"msg": "A Resume with this title already exists"})
            else:
                db["resumes"].insert_one({
                    "email": email,
                    "title": title,
                    "resume": {}
                })
                return redirect("resumeister_app:Upload Resume",str(title))
        else:
            return redirect("resumeister_app:Login")

# class Main(View):
#     def get(self,request):
#         if request.session.has_key('email'):
#             return redirect('/homepage_logged_in')
#         return render(request, 'resumeister_app/main.html')

def Logout(request):
    if request.session.has_key('email'):
        del request.session['email']
        request.session.modified = True
    return redirect("resumeister_app:Landing Page")

def CreateResume(request, resume):
    email = request.session.get("email")
    data = json.loads(json_util.dumps(db["resumes"].find_one({"email": email, "title": resume}, {"_id": 0})))
    data_str = json.dumps(data.get("resume"))
    print(data_str)
    response = render(request, 'resumeister_app/createResume.html', {"parse_data": data_str})
    response.set_cookie(key="title", value=resume)
    response.set_cookie(key="parse_data", value=data_str)
    return response

def DeleteResume(request, resume):
    email = request.session.get("email")
    db["resumes"].delete_one({"email": email, "title": resume})
    return redirect("resumeister_app:Homepage Logged In")

def handle_uploaded_file(f, filename):
    with open(filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def UploadResume(request, title):
    if request.method=='POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            name = str(request.FILES["file"].name)
            ext = name.split('.')[-1]
            filename = str('./ParsingApp/new_upload.' + ext)
            handle_uploaded_file(request.FILES["file"], filename)
            data = requests.get("http://127.0.0.1:5004/parse_resume", params={"file_path": filename}).json().get(
                "parsed_resume")
            response = render(request, 'resumeister_app/createResume.html')
            response.set_cookie(key="title", value=title)
            response.set_cookie(key="parse_data", value=data)
            response.set_cookie(key="extract_data", value="", expires=datetime.now())
            return response
        else:
            raise FileNotFoundError
    else:
        form = UploadFileForm()
        response =  render(request, 'resumeister_app/uploadResume.html', {"form": form, "title": title})
        response.set_cookie(key="title", value=title)
        return response


class SaveResume(View):
    def get(self, request):
        if request.session.has_key('email'):
            extract_data = request.COOKIES.get("extract_data")
            title = request.COOKIES.get("title")
            print(extract_data)
            resume_data = json.loads(extract_data)
            print(resume_data)
            set_dict = { "$set": { "resume": resume_data } }
            db["resumes"].update_one({"email": request.session.get("email"), "title": title}, set_dict)
            tex_content = format_to_tex(resume_data)
            output_tex = "./ParsingApp/new_test/formatted_resume.tex"
            save_to_tex(tex_content, output_tex)
            convert_latex_to_pdf(output_tex)
            output_file = "formatted_resume.pdf"
            with open(output_file, "rb") as fprb:
                response = HttpResponse(fprb.read(), content_type="pdf")
            response["Content-Disposition"] = "attachment; filename=" + title + ".pdf"
            response.set_cookie(key="extract_data", value="", expires=datetime.now())
            response.set_cookie(key="parse_data", value="", expires=datetime.now())
            response.set_cookie(key="title", value="", expires=datetime.now())
            return response
        else:
            return redirect("resumeister_app:Login")



def extract_skills_from_job_description(job_description):
    nlp = spacy.load('en_core_web_sm')
    
    # Init skill extractor
    skill_extractor = SkillExtractor(nlp, job_description, PhraseMatcher)

    # Annotate the job description to get skills
    annotations = skill_extractor.annotate()

    # Extract 'doc_node_value' from 'full_matches' and 'ngram_scored'
    doc_node_values = []

    # Extract 'doc_node_value' from 'full_matches'
    for item in annotations['results']['full_matches']:
        doc_node_values.append(item['doc_node_value'])

    # Extract 'doc_node_value' from 'ngram_scored'
    for item in annotations['results']['ngram_scored']:
        doc_node_values.append(item['doc_node_value'])

    return doc_node_values

class SkillExtractor:
    def __init__(self, nlp, job_description, phrase_matcher):
        self.nlp = nlp
        self.job_description = job_description
        self.matcher = phrase_matcher(nlp.vocab)
        self.matcher.add("SKILLS", None, *[nlp(skill) for skill in self.extract_skills_from_job()])

    def extract_skills_from_job(self):
        doc = self.nlp(self.job_description)
        # In this example, we'll extract nouns as skills from the job description
        return list(set(chunk.text for chunk in doc.noun_chunks))

    def annotate(self):
        doc = self.nlp(self.job_description)
        matches = self.matcher(doc)
        annotations = {"results": {"full_matches": [], "ngram_scored": []}}
        for match_id, start, end in matches:
            span = doc[start:end]
            annotations["results"]["full_matches"].append({"doc_node_value": span.text})
        return annotations

def extract_skills_view(request):
    if request.method == 'POST':
        job_description = request.POST.get('job_description', '')
        suggested_skills = extract_skills_from_job_description(job_description)
        return render(request, 'resumeister_app/skills.html', {'suggested_skills': suggested_skills})
    return render(request, 'resumeister_app/description.html')
