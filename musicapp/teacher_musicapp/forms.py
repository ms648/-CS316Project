from django.forms import ModelForm
from .models import Member
 
class MyStudentForm(ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'email']