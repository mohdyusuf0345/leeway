from django import forms
from .models import *

class Movie_Form(forms.ModelForm):
    class Meta:
        model = Movie_Model
        fields = '__all__'


'''
User Sign Up/Forgot Password APIs.
 Uses JWT authentication.
 Must define 3 user levels: 1. Super-admin, 2. Teacher, 3. Student (Use
internal Django Groups to achieve the same).
 Teacher must be able to add/list the students.
 Admin must be able to add/list every user in the database.
 Students must be able to see his information only.
 Code should be commented for clarity
'''