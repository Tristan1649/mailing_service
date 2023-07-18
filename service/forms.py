from django import forms
from .models import Campaign

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign # Указывает модель, с которой связана форма.
        fields = ('start_time', 'end_time', 'client_filter', 'message')
        #  Поля, которые будут отображаться в форме.
        
        #Определяет виджеты для отображения полей.
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    
            #который позволяет вводить дату и время в формате 
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            # (без учета часового пояса).
        }


