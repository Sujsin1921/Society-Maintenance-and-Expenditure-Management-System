from django import forms
from .models import expence

class ImageForm(forms.ModelForm):
    class Meta:
        model = expence
        fields=('title','description','expence_date','bill_amount','images')

        widgets={
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control','rows':'4'}),
            'expence_date': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'bill_amount': forms.NumberInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'})            
        }