from django import forms
from .models import chaiVarity

class chaiVarityForm(forms.Form):
    chai_varity=forms.ModelChoiceField(queryset=chaiVarity.objects.all(),label='Select Chai Varity')