from django.http import HttpResponse
from django.shortcuts import render
from .models import Profile, user, entry
from django.views.generic.edit import CreateView

# Create your views here.

def inicio(req):
    return render(req, "inicio.html")

def profiles(req):
    return render(req, "profiles.html")

def posts(req):
    return render(req, "posts.html")

def busqueda_profile(req):

    return render(req, "busqueda_profile.html")

def buscar_profile(req):

    if req.GET["user"]:
        user = req.GET["user"] 
        profile = Profile.objects.get(user=user)
        if profile:
            return render(req, "resultado_busqueda.html", {"profile": profile})
    else: 
        return HttpResponse('No escribiste ningún usuario')
    
def lista_users(req):

    users = user.objects.all()

    return render(req, "users_list.html", {"users": users})

def lista_profiles(req):

    profiles = Profile.objects.all()

    return render(req, "profiles_list.html", {"profiles": profiles})

def lista_entries(req):

    entries = entry.objects.all()

    return render(req, "entries_list.html", {"entries": entries})


class userCreate(CreateView):
    model = user
    template_name = "user_create.html"
    fields = ["name", "lastName", "age", "password", "email"]
    success_url = "/blog-tecnowave/"

class profileCreate(CreateView):
    model = Profile
    template_name = "profile_create.html"
    fields = ["title", "aboutMe", "socialMedia", "user"]
    success_url = "/blog-tecnowave/"

class entryCreate(CreateView):
    model = entry
    template_name = "entry_create.html"
    fields = ["title", "text"]
    success_url = "/blog-tecnowave/"