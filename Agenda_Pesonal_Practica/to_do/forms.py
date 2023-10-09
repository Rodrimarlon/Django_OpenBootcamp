from django.forms import ModelForm
from .models import To_Do

class To_DoForm(ModelForm):
    class Meta:
        model = To_Do
        fields = '__all__'