from django import forms
from .models import Student
from django.contrib.auth.forms import UserCreationForm


class StudentRegistrationForm(UserCreationForm):

    class Meta:
        model = Student
        fields = ['email', 'username', 'usn', 'year', 'branch', "phone_no"]
