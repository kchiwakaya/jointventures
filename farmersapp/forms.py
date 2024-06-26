from django import  forms
from .models import Farmer, Farm, Venture

class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ('name','othername','surname','phone','address','gender','national_id')

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','place_holder':'Name'}),
            'othername':forms.TextInput(attrs={'class':'form-control','place_holder':'Other Name'}),
            'surname':forms.TextInput(attrs={'class':'form-control','place_holder':'Surname'}),
            'phone':forms.TextInput(attrs={'class':'form-control','place_holder':'Phone'}),
            'address':forms.TextInput(attrs={'class':'form-control','place_holder':'Address'}),
            'gender':forms.Select(attrs={'class':'form-control','place_holder':'Gender'}),
            'national_id':forms.TextInput(attrs={'class':'form-control','place_holder':'National ID'})
        }


class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = ('farm_name','plot_number','extend','district',
                  'province','ward','tenure_type','irrigation','water_availability','description')
        
        widgets = {
            'farm_name':forms.TextInput(attrs={'class':'form-control'}),
            'plot_number':forms.TextInput(attrs={'class':'form-control'}),
            'extend':forms.TextInput(attrs={'class':'form-control'}),
            'district':forms.TextInput(attrs={'class':'form-control'}),
            'province':forms.Select(attrs={'class':'form-control'}),
            'ward':forms.TextInput(attrs={'class':'form-control'}),
            'tenure_type':forms.Select(attrs={'class':'form-control'}),
            'irrigation':forms.Select(attrs={'class':'form-control'}),
            'water_availability': forms.Select(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),

        }
        
      
class VentureForm(forms.ModelForm):
    class Meta:
        model = Venture
        fields = ('descripiton','supporting_images','amount')
    
        widgets = {
            'descripiton':forms.Textarea(attrs={'class':'form-control'}),
            'supporting_images':forms.TextInput(attrs={'class':'form-control'}),
            'amount':forms.TextInput(attrs={'class':'form-control'}),

        }
       