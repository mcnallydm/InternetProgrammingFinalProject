from django.http.response import HttpResponse
from django.http import Http404
from django.shortcuts import render
from datetime import datetime
from ..app.models import *
from django.views.generic import CreateView
#from .forms import *
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def index(request):
    return render(request, 'index.html')