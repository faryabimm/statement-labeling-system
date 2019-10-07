from django import forms


class LabelStatementForm(forms.Form):
    statement = forms.CharField(widget=forms.Textarea, disabled=True, label='statement', required=False)
    statement_id = forms.IntegerField(widget=forms.HiddenInput, required=True)
    initial_timestamp = forms.FloatField(widget=forms.HiddenInput, required=True)
