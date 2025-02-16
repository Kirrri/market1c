from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import LegalEntityForm

@login_required
def legal_entity_form(request):
    if request.method == 'POST':
        form = LegalEntityForm(request.POST)
        if form.is_valid():
            legal_entity = form.save(commit=False)
            legal_entity.user = request.user
            legal_entity.save()
            return redirect('profile')  # Перенаправляем в личный кабинет
    else:
        form = LegalEntityForm()

    return render(request, 'profile/legal_entity_form.html', {'form': form})

@login_required
def profile(request):
    user = request.user
    legal_entity = getattr(user, 'legal_entity', None)  # Получаем данные юридического лица, если они есть

    context = {
        'user': user,
        'legal_entity': legal_entity,
    }
    return render(request, 'profile/profile.html', context)
