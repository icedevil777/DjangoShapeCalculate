from django import forms
from .models import *


class AddPostForm(forms.Form):
    side = forms.CharField(max_length=255)

