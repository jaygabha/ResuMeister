from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
import pymongo
from utils import db
from django.urls import reverse
from urllib.parse import urlencode
from django.views import View

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
