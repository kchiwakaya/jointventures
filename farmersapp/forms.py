from django import  forms
from .models import Farmer, Farm, Venture

class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ('name','othername','surname','phone','address','gender','national_id')

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'othername':forms.TextInput(attrs={'class':'form-control'}),
            'surname':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.TextInput(attrs={'class':'form-control'}),
            'national_id':forms.TextInput(attrs={'class':'form-control'})
        }

class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = ('farm_name','plot_number','extend','district',
                  'province','ward','tenure_type','irrigation','water_availability')
        widgets = {
            'farm_name':forms.TextInput(attrs={'class':'form-control'}),
            'plot_number':forms.TextInput(attrs={'class':'form-control'}),
            'extend':forms.TextInput(attrs={'class':'form-control'}),
            'district':forms.TextInput(attrs={'class':'form-control'}),
            'province':forms.TextInput(attrs={'class':'form-control'}),
            'ward':forms.TextInput(attrs={'class':'form-control'}),
            'tenure_type':forms.TextInput(attrs={'class':'form-control'}),
            'irrigation':forms.TextInput(attrs={'class':'form-control'}),
            'water_availability': forms.TextInput(attrs={'class':'form-control'}),

        }
class VentureForm(forms.ModelForm):
    class Meta:
        model = Venture
        fields = ('farm','descripiton','supporting_images','amount')

        widgets = {
            'descripiton':forms.Textarea(attrs={'class':'form-control'}),
            'supporting_images':forms.TextInput(attrs={'class':'form-control'}),
            'amount':forms.TextInput(attrs={'class':'form-control'}),

        }