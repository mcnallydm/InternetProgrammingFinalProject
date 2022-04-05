"""ipfinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from app import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('spell_detail/<int:spell_id>/<str:spell_name>/', views.spell_detail, name="spell_detail"),
    path('class_spells/<str:class_name>/', views.class_spells, name="class_spells"),
    path('classes/', views.classes, name="classes"),
    path('school_spells/<str:school_name>/', views.school_spells, name="school_spells"),
    path('schools/', views.schools, name="schools"),
    path('level_spells/<int:level_num>/', views.level_spells, name="level_spells"),
    path('levels/', views.levels, name="levels"),
     path("login", views.LoginInterfaceView.as_view(), name="login"),
    path("logout", views.LogoutInterfaceView.as_view(), name="logout"),
    path("register", views.RegisterView.as_view(), name="register"),
    path('custom_spells/', views.custom_spells, name="custom_spells"),
    path("search", views.search, name="search"),
    path ("custom_spells/new", views.spellCreateView.as_view(), name="new_spell"),
    path('view_profile/', views.view_profile, name="view_profile"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)