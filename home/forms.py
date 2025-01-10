from django import forms


class CreateForm(forms.Form):
    title = forms.CharField(label='titles',required=False)
    body = forms.CharField()
    create = forms.DateTimeField()
