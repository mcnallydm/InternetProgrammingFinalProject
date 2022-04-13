from django import forms
from .models import *
from django.core.exceptions import ValidationError

class SpellForm(forms.ModelForm):
    class Meta:
        model = Spell
        fields = (
            'name', 
            'level', 
            'school',
            'range',
            'area',
            'area_shape',
            'attack',
            'saving_throw',
            'casting_time',
            'ritual',
            'duration',
            'concentration',
            'components',
            'materials',
            'damage_type',
            'description',
            'upcasting',
            'effects',
            'char_class',
        )

        widgets = {
            'name': forms.TextInput(attrs={"class": "col-auto form-control"}),
            'level': forms.NumberInput(attrs={"class": "col"}),
            'school': forms.RadioSelect(),
            'range': forms.TextInput(attrs={"class": "col"}),
            'area': forms.TextInput(attrs={"class": "col"}),
            'area_shape': forms.RadioSelect(),
            'attack': forms.RadioSelect(),
            'saving_throw': forms.RadioSelect(),
            'components': forms.CheckboxSelectMultiple(),
            'materials': forms.Textarea(attrs={"class": "col-auto form-control"}),
            'damage_type': forms.CheckboxSelectMultiple(),
            'effects': forms.CheckboxSelectMultiple(),
            'description': forms.Textarea(attrs={"class": "form-control"}),
            'upcasting': forms.Textarea(attrs={"class": "form-control mb-5"}),
            'char_class': forms.CheckboxSelectMultiple(),
        }
        labels = {
            'name': 'Spell Name:',
            'attack': "Attack Type:",
            'saving_throw': "Saving Throw:",
            'casting_time': "Casting Time:",
            'damage_type': "Damage Type:",
            'char_class': "Classes:",
        }

    def clean_school(self):
        sch = self.cleaned_data['school']
        if not sch:
            raise forms.ValidationError("You must select a school.")
        return sch
    
    def clean_level(self):
        lv = self.cleaned_data['level']
        if lv is None:
            raise forms.ValidationError("You must provide a level.")
        return lv

    def clean_name(self):
        name = self.cleaned_data['name']
        if not name:
            raise forms.ValidationError("You must provide a name.")
        if not name[0].isupper():
            raise forms.ValidationError("First letter should be capital.")
        return name