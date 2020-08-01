from django import forms
from .models import STATUS_CHOICES

default_status = STATUS_CHOICES[0][0]


BROWSER_DATETIME_FORMAT = '%Y-%m-%dT%H:%M'


class ReviewForm(forms.Form):
    author = forms.CharField(max_length=40, required=True, label='Автор', initial='Unknown')
    email = forms.EmailField(max_length=40, required=True, label='Почта')
    text = forms.CharField(max_length=3000, required=True, label="Текст", widget=forms.Textarea)
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=True, label='Статус', initial=default_status)

    # для полей типа DateField
    # publish_at = forms.DateField(..., widget=forms.DateInput(attrs={'type': 'date'}))
