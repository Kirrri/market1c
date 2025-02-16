from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

@login_required
def market(request):
    user = request.user

    # Проверяем, подтверждён ли email
    if not user.is_email_verified:
        return HttpResponseForbidden("Вы должны подтвердить email для доступа.")

    # Если пользователь юр. лицо, проверяем заполненность формы
    if user.user_type == 'legal' and not hasattr(user, 'legal_entity'):
        return HttpResponseForbidden("Юридические лица должны заполнить форму.")

    return render(request, 'market/market.html')