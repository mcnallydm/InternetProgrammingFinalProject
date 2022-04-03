from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Spell)
class SpellAdmin(admin.ModelAdmin):
    pass

@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    pass

@admin.register(DamageType)
class DamageAdmin(admin.ModelAdmin):
    pass

@admin.register(Effect)
class EffectAdmin(admin.ModelAdmin):
    pass

@admin.register(CharacterClass)
class CharClassAdmin(admin.ModelAdmin):
    pass

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    pass