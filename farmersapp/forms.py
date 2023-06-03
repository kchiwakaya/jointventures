from django.forms import ModelForm
from .models import Farmer, Farm, Venture

class FarmerForm(ModelForm):
    class Meta:
        model = Farmer
        fields = '__all__'

class FarmForm(ModelForm):
    class Meta:
        model = Farm
        fields = '__all__'

class VentureForm(ModelForm):
    class Meta:
        model = Venture
        fields = '__all__'