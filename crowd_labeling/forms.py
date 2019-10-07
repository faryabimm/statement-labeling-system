from django import forms

from .models import LabelChoices


class LabelStatementForm(forms.Form):
    statement = forms.CharField(widget=forms.Textarea, disabled=True, label='statement', required=False)
    statement_id = forms.IntegerField(widget=forms.HiddenInput, required=True)
    label = forms.ChoiceField(choices=LabelChoices.values_with_blank(), label='label', required=True)
    initial_timestamp = forms.FloatField(widget=forms.HiddenInput, required=True)
