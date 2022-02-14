from django import forms
from .models import *


class AddPostForm(forms.Form):
    side = forms.CharField(max_length=255)
    # img = forms.ImageField(null=True, blank=True, upload_to="static/calculate/img/square.png")

