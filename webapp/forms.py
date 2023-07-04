from cProfile import label
from dataclasses import fields
from secrets import choice
from .models import CustomUser,ApplicationModel
from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError


class CustomUserForm(ModelForm):
    cpassword=forms.CharField(widget=forms.PasswordInput(),label='confirm password')
    class Meta:
        model=CustomUser
        fields=('first_name','last_name','email','password','cpassword','role')
        widgets={'password':forms.PasswordInput(),}

    def clean(self):
        cleaned_data = super(CustomUserForm, self).clean()
        password=cleaned_data.get('password')
        cpassword=cleaned_data.get('cpassword')
        if(password!=cpassword):
            raise ValidationError('passwords should be same')
     


class LoginForm(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())
    # role_choice=[('','-----------'),('student','student'),('faculty','faculty')]
    # role=forms.ChoiceField(choices=role_choice)


class ApplicationForm(ModelForm):
    class Meta:
        model=ApplicationModel
        fields=('uni_name','program_name','study_mode')