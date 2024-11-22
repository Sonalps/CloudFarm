# Generated by Django 5.1.3 on 2024-11-20 13:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloudfarm_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fertilizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('suitable_crops', models.TextField(help_text='Comma-separated list of suitable crops')),
                ('image', models.ImageField(upload_to='fertilizer_images/')),
            ],
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='number',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(code='invalid_phone_number', message='Phone number must be exactly 10 digits.', regex='^\\d{10}$')]),
        ),
    ]