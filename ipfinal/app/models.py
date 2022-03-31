from time import time
from django.db import models

# Create your models here.

class Spell(models.Model):
    name = models.CharField(max_length=20)
    level = models.IntegerField(minimum=0)
    description = models.CharField(max_length=4000)
    '''
    school
    components
    range
    area
    att_save
    casting_time
    duration
    damage_types
    effects
    concentration
    '''

    def __str__(self):
        return f"{self.id}:{self.name}"