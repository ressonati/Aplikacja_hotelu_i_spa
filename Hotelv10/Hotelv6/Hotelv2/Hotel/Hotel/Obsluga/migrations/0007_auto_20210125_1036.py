# Generated by Django 3.1.5 on 2021-01-25 09:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Obsluga', '0006_remove_pokoj_czy_dostawka'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokoj',
            name='img',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='pobyt',
            name='data_zakwaterowania',
            field=models.DateField(default=datetime.date(2021, 1, 25), verbose_name='Data_zakwaterowania'),
        ),
        migrations.AlterField(
            model_name='rezerwacja_pokoju',
            name='dodatkowe_uslugi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Obsluga.dodatkowe_uslugi'),
        ),
        migrations.AlterField(
            model_name='rezerwacja_pokoju',
            name='pobyt',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Obsluga.pobyt'),
        ),
    ]
