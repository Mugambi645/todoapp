from django import forms
from .models import Work
class todosform(forms.ModelForm):
    class Meta:
        model = Work
        fields = "__all__"