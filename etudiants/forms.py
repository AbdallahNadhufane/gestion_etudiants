from django import forms
from .models import Etudiant


class EtudiantForm(forms.ModelForm):

    class Meta:
        model = Etudiant
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
