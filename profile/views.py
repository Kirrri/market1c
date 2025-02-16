from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import LegalEntity
from .forms import LegalEntityForm
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.conf import settings
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse
from market1c.models import CustomUser
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator


@login_required
def legal_entity_form(request):
    # Получаем существующие данные, если они есть
    legal_entity, created = LegalEntity.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = LegalEntityForm(request.POST, instance=legal_entity)  # Передаём instance
        if form.is_valid():
            form.save()
            return redirect('profile')  # Перенаправляем в личный кабинет
    else:
        form = LegalEntityForm(instance=legal_entity)  # Загружаем данные в форму

    return render(request, 'profile/legal_entity_form.html', {'form': form})

@login_required
def profile(request):
    user = request.user
    legal_entity = getattr(user, 'legal_entity', None)  # Получаем данные юридического лица, если они есть

    context = {
        'user': user,
        'legal_entity': legal_entity,
        'is_legal': user.user_type == 'legal',
    }
    return render(request, 'profile/profile.html', context)

@login_required
def send_verification_email(request):
    user = request.user
    if user.is_email_verified:
        return HttpResponse("Ваш email уже подтверждён.", status=400)

    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    verification_link = request.build_absolute_uri(reverse('verify_email', args=[uid, token]))

    send_mail(
        subject="Подтверждение email",
        message=f"Для подтверждения email перейдите по ссылке: {verification_link}",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        fail_silently=False,
    )

    return HttpResponse("Ссылка для подтверждения отправлена на ваш email.")



def verify_email(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None

    if user and default_token_generator.check_token(user, token):
        user.is_email_verified = True
        user.save()
        return HttpResponse("Ваш email успешно подтверждён!")
    else:
        return HttpResponse("Неверная или устаревшая ссылка.", status=400)
