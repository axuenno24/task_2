# Generated by Django 5.1.3 on 2024-11-20 15:06

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
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('Новая', 'New'), ('Принято', 'Accept'), ('Выполнено', 'Done')], default='Новая', max_length=50, verbose_name='Статус заказа')),
                ('photo', models.ImageField(default=None, null=True, upload_to='image/', verbose_name='Изображение категории')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Заказы',
                'verbose_name_plural': 'Заказы',
                'ordering': ['-time_create'],
                'indexes': [models.Index(fields=['-time_create'], name='orders_orde_time_cr_d24381_idx')],
            },
        ),
    ]
