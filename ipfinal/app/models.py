from time import time
from xml.parsers.expat import model
from django.db import models
from django.forms import IntegerField

# Create your models here.
class School(models.Model):
    school = models.CharField(max_length=30, blank=True)
    def __str__(self):
        return f"{self.id}: {self.school}"

class Component(models.Model):
    COMPONENT_TYPES = [("V", "Verbal"), ("S", "Somatic"), ("M", "Material")]
    components = models.CharField(max_length=20, choices=COMPONENT_TYPES, default="None")
    
    def __str__(self):
        return f"{self.id}: {self.components}"

class DamageType(models.Model):
    damage_type = models.CharField(max_length=30, default="None")
    def __str__(self):
        return f"{self.id}: {self.damage_type}"

class Effect(models.Model):
    effects = models.CharField(max_length=30, default="None")
    def __str__(self):
        return f"{self.id}: {self.effects}"

class CharacterClass(models.Model):
    char_class = models.CharField(max_length=70, null=True)
    def __str__(self):
        return f"{self.id}: {self.char_class}"

class Spell(models.Model):
    name = models.CharField(max_length=20)
    level = models.IntegerField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    materials = models.CharField(max_length=100, default="None")
    range = models.IntegerField()
    area = models.IntegerField()
    AREA_TYPES = [("N", "None"), ("R", "Radius"), ("C", "Cube"), ("S", "Sphere"), ("Y", "Cylinder")]
    area_shape = models.CharField(max_length=20, choices=AREA_TYPES, default="None")
    ATTACK_TYPES = [
        ("M", "Melee Spell Attack"), 
        ("R", "Ranged Spell Attack"), 
        ("D", "Dexterity Save"), 
        ("S", "Strength Save"),
        ("C", "Constitution Save"),
        ("I", "Intelligence Save"),
        ("W", "Wisdom Save"),
        ("H", "Charisma Save"),
        ("N", "None")
    ]
    att_save = models.CharField(max_length=30, choices=ATTACK_TYPES, default="None")
    casting_time = models.CharField(max_length=20, default="None")
    duration = models.CharField(max_length=20, default="None")
    concentration = models.BooleanField()
    components = models.ManyToManyField(Component, blank=True)
    damage_type = models.ManyToManyField(DamageType, blank=True)
    effects = models.ManyToManyField(Effect, blank=True)
    description = models.TextField(max_length=4000, default="No description provided.")
    upcasting = models.TextField(max_length=1000, default="You may not upcast this spell.")
    char_class = models.ManyToManyField(CharacterClass, blank=True)
    RATING_OPTIONS = [(0, "No Rating"), (1, "1/5"), (2, "2/5"), (3, "3/5"), (4, "4/5"), (5, "5/5")]
    rating = models.IntegerField(choices=RATING_OPTIONS, null = True, blank=True)

    def __str__(self):
        return f"{self.id}: {self.name}"



'''class School(models.Model):
    school = models.CharField(max_length=30, default="None")'''