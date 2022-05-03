from django import forms
from .models import Alvo

class AlvoForm(forms.ModelForm):
    class Meta:
        model = Alvo
        fields = "__all__"