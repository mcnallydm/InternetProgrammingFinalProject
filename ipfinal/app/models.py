from operator import truediv
from time import time
from xml.parsers.expat import model
from django.db import models
from django.forms import IntegerField
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=30, blank=True)
    def __str__(self):
        return f"{self.name}"

class Component(models.Model):
    COMPONENT_TYPES = [("V", "Verbal"), ("S", "Somatic"), ("M", "Material")]
    name = models.CharField(max_length=20, choices=COMPONENT_TYPES, default="None")
    
    def __str__(self):
        return f"{self.name}"

class DamageType(models.Model):
    name = models.CharField(max_length=30, default="None")
    def __str__(self):
        return f"{self.name}"

class Effect(models.Model):
    name = models.CharField(max_length=30, default="None")
    def __str__(self):
        return f"{self.name}"

class CharacterClass(models.Model):
    name = models.CharField(max_length=70, null=True)
    def __str__(self):
        return f"{self.name}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(max_length=1000, blank=True)
    avatar = models.ImageField(default='default.png', upload_to='profile_images')
    def __str__(self):
        return f"{self.user.username}"

class Spell(models.Model):
    name = models.CharField(max_length=40)
    level = models.IntegerField(help_text = "Enter 0 for cantrips")
    school = models.ForeignKey(School, related_name="spell", on_delete=models.CASCADE)
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
    components = models.ManyToManyField(Component, related_name="spell", blank=True)
    materials = models.TextField(max_length=500, default="None")
    damage_type = models.ManyToManyField(DamageType, related_name="spell", blank=True)
    effects = models.ManyToManyField(Effect, blank=True)
    description = models.TextField(max_length=4000, default="No description provided.")
    upcasting = models.TextField(max_length=1000, default="No additional effects when upcast.")
    char_class = models.ManyToManyField(CharacterClass, related_name="spell", blank=True)
    creator = models.ForeignKey(Profile, related_name="created_spells", blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

class Rating(models.Model):
    spell = models.ForeignKey(Spell, related_name="rating", blank=True, on_delete=models.CASCADE)
    player = models.ForeignKey(Profile, related_name="rating", blank=True, on_delete=models.CASCADE)
    favorite = models.BooleanField(default=False)
    score = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return f"{self.player.user.username} / {self.spell}"