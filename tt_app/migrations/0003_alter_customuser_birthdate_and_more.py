# Generated by Django 5.0.6 on 2024-05-19 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tt_app', '0002_alter_customuser_birthdate_alter_customuser_dni_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='birthdate',
            field=models.DateField(blank=True, default='1990-01-01', error_messages={'required': 'Por favor ingresá tu fecha de nacimiento'}),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, error_messages={'required': 'Por favor ingresá tu fecha de nacimiento'}, verbose_name='date joined'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, error_messages={'required': 'Por favor ingresá tu nombre'}, max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, error_messages={'required': 'Por favor ingresá tu apellido'}, max_length=50),
        ),
    ]
