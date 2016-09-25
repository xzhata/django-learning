from django import forms

class addform(forms.Form):
    busid = forms.CharField(max_length=10)
    token = forms.CharField(max_length=50)
    usr_name = forms.CharField(max_length=12)
    filepath = forms.FileField()
