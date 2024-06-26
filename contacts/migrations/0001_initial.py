# Generated by Django 5.0.3 on 2024-03-26 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('is_helium', models.BooleanField(default=False, verbose_name='С гелием')),
                ('is_painted', models.BooleanField(default=False, verbose_name='С рисунком')),
                ('is_metallic', models.BooleanField(default=False, verbose_name='Металлик')),
                ('is_foil', models.BooleanField(default=False, verbose_name='Фольгированный')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
                'ordering': ['-created_at'],
            },
        ),
    ]
