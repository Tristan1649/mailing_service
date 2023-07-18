from django.shortcuts import render, redirect
from .forms import CampaignForm

def campaign_form_view(request):
    if request.method == 'POST':
        form = CampaignForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('campaign_form')  # Перенаправление на ту же страницу после успешной отправки
    
    else:
        form = CampaignForm()

    return render(request, 'campaign_form.html', {'form': form})


# campaign_form_view - представление Django для создания 
# и сохранения новой рассылки через веб-форму. 
# Если запрос методом POST, данные сохраняются в базе данных 
# и происходит перенаправление на страницу формы. 
# Если запрос методом GET, 
# отображается пустая форма для заполнения данных.