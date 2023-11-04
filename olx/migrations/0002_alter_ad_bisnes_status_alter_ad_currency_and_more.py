# Generated by Django 4.2.6 on 2023-11-03 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olx', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='bisnes_status',
            field=models.CharField(choices=[('Jismoniy', 'Phisical'), ('Biznes', 'Biznes')], default='Jismoniy', max_length=255),
        ),
        migrations.AlterField(
            model_name='ad',
            name='currency',
            field=models.CharField(choices=[('UZS', 'Uzs'), ('USD', 'Usd')], default='UZS', max_length=255),
        ),
        migrations.AlterField(
            model_name='ad',
            name='status',
            field=models.CharField(choices=[('Yangi', 'New'), ('F/B', 'Fb')], default='Yangi', max_length=255),
        ),
    ]