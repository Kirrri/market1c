# Generated by Django 5.1.6 on 2025-02-16 14:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LegalEntity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inn', models.CharField(max_length=12, verbose_name='ИНН')),
                ('organization_name', models.CharField(max_length=255, verbose_name='Наименование организации')),
                ('ownership_form', models.CharField(choices=[('ИП', 'Индивидуальный предприниматель (ИП)'), ('ООО', 'Общество с ограниченной ответственностью (ООО)'), ('АО', 'Акционерное общество (АО)'), ('ЗАО', 'Закрытое акционерное общество (ЗАО)'), ('ОАО', 'Открытое акционерное общество (ОАО)')], max_length=50, verbose_name='Форма собственности')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('address', models.CharField(verbose_name='Адрес')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='legal_entity', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
