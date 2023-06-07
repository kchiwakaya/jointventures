from django import  forms
from .models import Farmer, Farm, Venture

class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = '__all__'

class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = '__all__'

class VentureForm(forms.ModelForm):
    class Meta:
        model = Venture
        fields = '__all__'
        #fields = ('farm','descripiton','supporting_images','amount')

        #widgets = {
            #'farm':forms.TextInput(attrs={'class':'form-control'}),
            #'descripiton':forms.Textarea(attrs={'class':'form-control'}),
            #'supporting_images':forms.TextInput(attrs={'class':'form-control'}),
            #'amount':forms.TextInput(attrs={'class':'form-control'}),

        #}