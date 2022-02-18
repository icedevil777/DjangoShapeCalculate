from django import forms


class OneForm(forms.Form):
    side_x = forms.IntegerField(min_value=0, max_value=1000, widget=forms.TextInput)


class TwoForms(forms.Form):
    side_x = forms.IntegerField(min_value=0, max_value=10000)
    side_y = forms.IntegerField(min_value=0, max_value=10000)


class ThreeForms(forms.Form):
    side_x = forms.IntegerField(min_value=0, max_value=10000)
    side_y = forms.IntegerField(min_value=0, max_value=10000)
    side_z = forms.IntegerField(min_value=0, max_value=10000)


