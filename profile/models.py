from django.conf import settings
from django.db import models

class LegalEntity(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='legal_entity')
    inn = models.CharField(max_length=12, verbose_name='ИНН')
    organization_name = models.CharField(max_length=255, verbose_name='Наименование организации')
    ownership_form = models.CharField(
        max_length=50,
        choices=[
            ('ИП', 'Индивидуальный предприниматель (ИП)'),
            ('ООО', 'Общество с ограниченной ответственностью (ООО)'),
            ('АО', 'Акционерное общество (АО)'),
            ('ЗАО', 'Закрытое акционерное общество (ЗАО)'),
            ('ОАО', 'Открытое акционерное общество (ОАО)'),
        ],
        verbose_name='Форма собственности'
    )
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    address = models.CharField(verbose_name='Адрес')

    def __str__(self):
        return f"{self.organization_name} ({self.inn})"