from django.http.response import HttpResponse
from django.http import Http404, JsonResponse
from django.shortcuts import render
from datetime import datetime
from .models import *
from django.views.generic import CreateView
from .forms import *
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    og = Profile.objects.get(id=1)
    spells = Spell.objects.filter(creator=og)
    results = spells.order_by('name')
    faves=[]
    try:
        curr_user = Profile.objects.get(user=request.user)
        faves = Rating.objects.filter(player=curr_user).filter(favorite=True)
    except:
        pass
    return render(request, 'index.html', {
        "v_spells" : results,
        "v_faves": faves,
        "v_classes" : CharacterClass.objects.all().order_by('name'),
        "v_schools" : School.objects.all(),
        "v_levels" : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    })

def spell_detail(request, spell_id, spell_name):
    faves=[]
    try:
        curr_user = Profile.objects.get(user=request.user)
        faves = Rating.objects.filter(player=curr_user).filter(favorite=True)
    except:
        pass
    rate=-1
    try:
        curr_user = Profile.objects.get(user=request.user)
        s = Spell.objects.get(id=spell_id)
        rated = Rating.objects.filter(player=curr_user).get(spell=s)
        rate=rated.score
    except:
        pass
    try:
        spell_to_view = Spell.objects.get(id=spell_id)
    except Spell.DoesNotExist:
        raise Http404('Spell not found.')
    return render(request, "spell_detail.html", {
        "v_spell" : spell_to_view,
        "v_faves": faves,
        "v_rate": rate,
        "v_classes" : CharacterClass.objects.all().order_by('name'),
        "v_schools" : School.objects.all(),
        "v_levels" : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    })

def class_spells(request, class_name):
    faves=[]
    try:
        curr_user = Profile.objects.get(user=request.user)
        faves = Rating.objects.filter(player=curr_user).filter(favorite=True)
    except:
        pass
    try:
        class_to_view = CharacterClass.objects.get(name=class_name)
    except CharacterClass.DoesNotExist:
        raise Http404('Class not found.')
    #results = Spell.objects.filter(char_class__contains = class_to_view)
    results = class_to_view.spell.all
    return render(request, "index.html", {
        "v_spells" : results,
        "v_faves": faves,
        "v_classes" : CharacterClass.objects.all().order_by('name'),
        "v_schools" : School.objects.all(),
        "v_levels" : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    })

def classes(request):
    return render(request, "classes.html", {
        "v_classes" : CharacterClass.objects.all().order_by('name'),
        "v_schools" : School.objects.all(),
        "v_levels" : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    })

def school_spells(request, school_name):
    faves=[]
    try:
        curr_user = Profile.objects.get(user=request.user)
        faves = Rating.objects.filter(player=curr_user).filter(favorite=True)
    except:
        pass
    try:
        school_to_view = School.objects.get(name=school_name)
    except CharacterClass.DoesNotExist:
        raise Http404('School not found.')
    results = school_to_view.spell.all
    return render(request, "index.html", {
        "v_spells" : results,
        "v_faves": faves,
        "v_classes" : CharacterClass.objects.all().order_by('name'),
        "v_schools" : School.objects.all(),
        "v_levels" : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    })

def schools(request):
    return render(request, "schools.html", {
        "v_classes" : CharacterClass.objects.all().order_by('name'),
        "v_schools" : School.objects.all(),
        "v_levels" : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    })

def level_spells(request, level_num):
    faves=[]
    try:
        curr_user = Profile.objects.get(user=request.user)
        faves = Rating.objects.filter(player=curr_user).filter(favorite=True)
    except:
        pass
    try:
        results = Spell.objects.filter(level=level_num)
    except Spell.DoesNotExist:
        raise Http404('Spell Level not found.')
    return render(request, "index.html", {
        "v_spells" : results,
        "v_faves": faves,
        "v_classes" : CharacterClass.objects.all().order_by('name'),
        "v_schools" : School.objects.all(),
        "v_levels" : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    })

def levels(request):
    return render(request, "levels.html", {
        "v_classes" : CharacterClass.objects.all().order_by('name'),
        "v_schools" : School.objects.all(),
        "v_levels" : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    })

@login_required
def custom_spells(request):
    faves=[]
    try:
        curr_user = Profile.objects.get(user=request.user)
        faves = Rating.objects.filter(player=curr_user).filter(favorite=True)
    except:
        pass
    try:
        curr_user = Profile.objects.get(user=request.user)
        spells_to_view = Spell.objects.filter(creator=curr_user)
    except Spell.DoesNotExist:
        raise Http404('User not found.')
    results = spells_to_view
    return render(request, "index.html", {
        "v_spells" : results,
        "v_faves": faves,
        "v_classes" : CharacterClass.objects.all().order_by('name'),
        "v_schools" : School.objects.all(),
        "v_levels" : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    })

@login_required
def favorites(request):
    faves=[]
    try:
        curr_user = Profile.objects.get(user=request.user)
        faves = Rating.objects.filter(player=curr_user).filter(favorite=True)
    except:
        pass
    try:
        curr_user = Profile.objects.get(user=request.user)
        faves = Rating.objects.filter(player=curr_user).filter(favorite=True)
        spells_to_view = []
        for rat in faves:
            spells_to_view.append(rat.spell)
    except Spell.DoesNotExist:
        raise Http404('User not found.')
    results = spells_to_view
    return render(request, "index.html", {
        "v_spells" : results,
        "v_faves": faves,
        "v_classes" : CharacterClass.objects.all().order_by('name'),
        "v_schools" : School.objects.all(),
        "v_levels" : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    })

@login_required
def view_profile(request):
    faves=[]
    try:
        curr_user = Profile.objects.get(user=request.user)
        faves = Rating.objects.filter(player=curr_user).filter(favorite=True)
    except:
        pass
    prof = Profile.objects.get(user=request.user)
    faves = Rating.objects.filter(player=prof).filter(favorite=True)
    my_faves = []
    for rat in faves:
        my_faves.append(rat.spell)
    my_spells = prof.created_spells.all
    return render(request, "view_profile.html", {
        "v_prof": prof,
        "v_faves": faves,
        "v_myfaves": my_faves,
        "v_cspells": my_spells,
        "v_classes" : CharacterClass.objects.all().order_by('name'),
        "v_schools" : School.objects.all(),
        "v_levels" : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    })

@login_required
def edit_bio(request):
    if request.method == "POST":
        bio = request.POST["bio"]
        prof = Profile.objects.get(user=request.user)
        prof.bio = bio
        prof.save()
        return JsonResponse({"msg": "ok"}, status=200)
    else:
        return render(request, "index.html")

def search(request):
    faves=[]
    try:
        curr_user = Profile.objects.get(user=request.user)
        faves = Rating.objects.filter(player=curr_user).filter(favorite=True)
    except:
        pass
    if request.method == "POST":
        keyword = request.POST["q"]
    try:
        og = Profile.objects.get(id=1)
        curr_user=Profile.objects.get(user=request.user)
        if keyword.lower()=="ritual":
                results = Spell.objects.filter(ritual=True).filter(creator=og)|Spell.objects.filter(ritual=True).filter(creator=curr_user)
        elif keyword.lower()=="concentration":
            results = Spell.objects.filter(concentration=True).filter(creator=og)|Spell.objects.filter(concentration=True).filter(creator=curr_user)
        else:
            results = Spell.objects.filter(name__contains = keyword).filter(creator=og) | \
                Spell.objects.filter(description__contains = keyword).filter(creator=og) | \
                Spell.objects.filter(upcasting__contains = keyword).filter(creator=og) | \
                Spell.objects.filter(name__contains = keyword).filter(creator=curr_user) | \
                Spell.objects.filter(description__contains = keyword).filter(creator=curr_user) | \
                Spell.objects.filter(upcasting__contains = keyword).filter(creator=curr_user)
    except TypeError:
        if keyword.lower()=="ritual":
                results = Spell.objects.filter(ritual = True).filter(creator=Profile.objects.get(id=1))
        elif keyword.lower()=="concentration":
            results = Spell.objects.filter(concentration = True).filter(creator=Profile.objects.get(id=1))
        else:
            results = Spell.objects.filter(name__contains = keyword) | \
                Spell.objects.filter(description__contains = keyword) | \
                Spell.objects.filter(upcasting__contains = keyword).filter(creator=Profile.objects.get(id=1))
    return render(request, "index.html", {
        "v_spells" : results,
        "v_faves": faves,
        "v_classes" : CharacterClass.objects.all().order_by('name'),
        "v_schools" : School.objects.all(),
        "v_levels" : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    })

@login_required    
def new_favorite(request):
    if request.method == "POST":
        favorite_str = request.POST["favorite"]
        if favorite_str=="True":
            favorite = True
        else:
            favorite=False
        spell_id = request.POST["spell_id"]
        spell = Spell.objects.get(id=spell_id)
        faved_by = Profile.objects.get(user=request.user)
        try:
            temp = Rating.objects.filter(spell=spell).get(player=faved_by)
            temp.favorite = favorite
        except:
            temp = Rating(spell=spell, player=faved_by, favorite=favorite)
        temp.save()
        return JsonResponse({"msg": "ok"}, status=200)
    else:
        return render(request, "index.html")

@login_required    
def new_rating(request):
    if request.method == "POST":
        rating = int(request.POST["rating"])
        spell_id = int(request.POST["spell_id"])
        spell = Spell.objects.get(id=spell_id)
        faved_by = Profile.objects.get(user=request.user)
        try:
            temp = Rating.objects.filter(spell=spell).get(player=faved_by)
            temp.score = rating
        except:
            temp = Rating(spell=spell, player=faved_by, score=rating)
        temp.save()
        return JsonResponse({"msg": "ok"}, status=200)
    else:
        return render(request, "index.html")

def delete_spell(request):
    if request.method == "POST":
        spell_id = int(request.POST["spell_id"])
        temp = Spell.objects.get(id=spell_id)
        temp.delete()
        return JsonResponse({"msg": "ok"}, status=200)
    else:
        return render(request, "index.html")

'''@login_required
def recommendations(request):
    '''

class spellCreateView(LoginRequiredMixin, CreateView):
    template_name = 'spell_form.html'
    model = Spell
    success_url = "/custom_spells"
    form_class = SpellForm
    login_url = "/login"
    def form_valid(self, form):
        form.instance.creator = Profile.objects.get(user=self.request.user)
        return super().form_valid(form)

class LoginInterfaceView(LoginView):
    template_name = 'login.html'
    extra_content = {'today': datetime.today()}
    success_url = ''

class LogoutInterfaceView(LogoutView):
    template_name = 'logout.html'

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = '/'