from django.http.response import HttpResponse
from django.http import Http404
from django.shortcuts import render
from datetime import datetime
from .models import *
from django.views.generic import CreateView
#from .forms import *
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def index(request):
    curr_user = request.user
    return render(request, 'index.html', {
        "v_spells" : Spell.objects.filter(user=1)|Spell.objects.filter(user=curr_user.id),
        "v_classes" : CharacterClass.objects.all(),
        "v_schools" : School.objects.all()
    })

def spell_detail(request, spell_name):
    try:
        spell_to_view = Spell.objects.get(name=spell_name)
    except Spell.DoesNotExist:
        raise Http404('Spell not found.')
    return render(request, "spell_detail.html", {
        "v_spell" : spell_to_view,
        "v_classes" : CharacterClass.objects.all(),
        "v_schools" : School.objects.all()
    })

def class_spells(request, class_name):
    try:
        class_to_view = CharacterClass.objects.get(name=class_name)
    except CharacterClass.DoesNotExist:
        raise Http404('Class not found.')
    #results = Spell.objects.filter(char_class__contains = class_to_view)
    results = class_to_view.spell.all
    return render(request, "index.html", {
        "v_spells" : results,
        "v_classes" : CharacterClass.objects.all(),
        "v_schools" : School.objects.all()
    })

def classes(request):
    return render(request, "classes.html", {
        "v_classes" : CharacterClass.objects.all(),
        "v_schools" : School.objects.all(),
    })

def school_spells(request, school_name):
    try:
        school_to_view = School.objects.get(name=school_name)
    except CharacterClass.DoesNotExist:
        raise Http404('School not found.')
    results = school_to_view.spell.all
    return render(request, "index.html", {
        "v_spells" : results,
        "v_classes" : CharacterClass.objects.all(),
        "v_schools" : School.objects.all()
    })

def schools(request):
    return render(request, "schools.html", {
        "v_classes" : CharacterClass.objects.all(),
        "v_schools" : School.objects.all(),
    })

def level_spells(request, level_num):
    try:
        results = Spell.objects.filter(level=level_num)
    except Spell.DoesNotExist:
        raise Http404('Spell Level not found.')
    return render(request, "index.html", {
        "v_spells" : results,
        "v_classes" : CharacterClass.objects.all(),
        "v_schools" : School.objects.all(),
        "v_levels" : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    })

def levels(request):
    return render(request, "levels.html", {
        "v_classes" : CharacterClass.objects.all(),
        "v_schools" : School.objects.all(),
        "v_levels" : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    })

def custom_spells(request):
    try:
        curr_user = request.user
        spells_to_view = Spell.objects.filter(user=curr_user.id)
    except CharacterClass.DoesNotExist:
        raise Http404('User not found.')
    results = spells_to_view
    return render(request, "index.html", {
        "v_spells" : results,
        "v_classes" : CharacterClass.objects.all(),
        "v_schools" : School.objects.all()
    })

class LoginInterfaceView(LoginView):
    template_name = 'login.html'
    extra_content = {'today': datetime.today()}
    success_url = ''

class LogoutInterfaceView(LogoutView):
    template_name = 'logout.html'

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = ''