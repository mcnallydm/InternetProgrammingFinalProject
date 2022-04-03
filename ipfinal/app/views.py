from django.http.response import HttpResponse
from django.http import Http404
from django.shortcuts import render
from datetime import datetime
from .models import *
from django.views.generic import CreateView
#from .forms import *
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def index(request):
    spells = Spell.objects.all()
    return render(request, 'index.html', {
        "v_spells" : spells
    })

def spell_detail(request, spell_id):
    spell_to_view = Spell.objects.get(id=spell_id)
    return render(request, "spell_detail.html", {
        "v_spell" : spell_to_view
    })