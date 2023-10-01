from django.forms import ModelForm
from .models import Employee

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        # incluir solo los que necesitemos
       #fiels = ['name', 'last_name'] 
        
        # para imcluirlos todos 
        fields = '__all__'
        
        # si queremos agragar otros 
       #extra_fields = [] 
        
        #si queremos agragarlos todos excluyendo solo algunos
       #exclude = ('email',)