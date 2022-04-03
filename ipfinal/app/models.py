from time import time
from xml.parsers.expat import model
from django.db import models
from django.forms import IntegerField

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=30, blank=True)
    def __str__(self):
        return f"{self.id}: {self.name}"

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
    range = models.CharField(max_length=20, default="Touch")
    area = models.CharField(max_length=30, default="Target")
    AREA_TYPES = [
        ("None", "None"), 
        ("Radius", "Radius"), 
        ("Cube", "Cube"), 
        ("Sphere", "Sphere"), 
        ("Cylinder", "Cylinder"), 
        ("Cone", "Cone")
        ]
    area_shape = models.CharField(max_length=20, choices=AREA_TYPES, default="None")
    ATTACK_TYPES = [
        ("None", "None"),
        ("Melee", "Melee Spell Attack"), 
        ("Ranged", "Ranged Spell Attack")
    ]
    SAVE_TYPES = [
        ("None", "None"),
        ("Dexterity", "Dexterity Save"), 
        ("Strength", "Strength Save"),
        ("Constitution", "Constitution Save"),
        ("Intelligence", "Intelligence Save"),
        ("Wisdom", "Wisdom Save"),
        ("Charisma", "Charisma Save")
    ]
    attack = models.CharField(max_length=30, choices=ATTACK_TYPES, default="None")
    saving_throw = models.CharField(max_length=30, choices=SAVE_TYPES, default="None")
    casting_time = models.CharField(max_length=20, default="None")
    ritual = models.BooleanField(default=False)
    duration = models.CharField(max_length=20, default="None")
    concentration = models.BooleanField()
    components = models.ManyToManyField(Component, blank=True)
    damage_type = models.ManyToManyField(DamageType, blank=True)
    effects = models.ManyToManyField(Effect, blank=True)
    description = models.TextField(max_length=4000, default="No description provided.")
    upcasting = models.TextField(max_length=1000, default="No additional effects when upcast.")
    char_class = models.ManyToManyField(CharacterClass, blank=True)
    RATING_OPTIONS = [
        ("No Rating", "No Rating"), 
        ("1/5", "1/5"), 
        ("2/5", "2/5"), 
        ("3/5", "3/5"), 
        ("4/5", "4/5"), 
        ("5/5", "5/5")
        ]
    rating = models.IntegerField(choices=RATING_OPTIONS, null = True, blank=True)
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}: {self.name}"