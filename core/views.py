from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PresenceForm
from .models import PresenceModel

def presenceForm(request):
    if request.method == 'POST':
        form = PresenceForm(request.POST)
        if form.is_valid():
            presence = form.save(commit=False)
            presence.save()
            messages.success(request, 'Presença registrada com sucesso!')
            return redirect('/')
        else:
            messages.error(request, 'Error: {}'.format(form.errors))
    else:
        form = PresenceForm()
        
    return render(request, 'form.html', {'form': PresenceForm()})