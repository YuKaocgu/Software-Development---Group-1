from django.forms import ModelForm
from Camper.models import Camper

# Create the form class.
class CamperForm(ModelForm):
     class Meta:
        model = Camper
        fields = ['name', 'age', 'gender', 'category', 'rank']