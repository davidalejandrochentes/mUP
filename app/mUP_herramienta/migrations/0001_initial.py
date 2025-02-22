# Generated by Django 5.1.1 on 2024-09-23 17:51

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Herramienta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('número_de_serie', models.CharField(max_length=100)),
                ('encargado', models.CharField(max_length=100)),
                ('teléfono_encargado', models.CharField(max_length=100)),
                ('descripción', models.TextField(max_length=500)),
                ('fecha_de_adquisición', models.DateField(default=datetime.date.today)),
                ('costo', models.IntegerField()),
                ('proveedor', models.CharField(max_length=100)),
                ('ubicación', models.CharField(max_length=100)),
                ('estado_de_la_herramienta', models.CharField(max_length=100)),
                ('fecha_ultimo_mantenimiento', models.DateField(default=datetime.date.today)),
                ('intervalo_mantenimiento', models.IntegerField(blank=True, default=0, null=True)),
                ('image', models.ImageField(upload_to='herramienta/image')),
            ],
        ),
        migrations.CreateModel(
            name='TipoMantenimientoHerramienta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MantenimientoHerramienta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('hora', models.TimeField(default=datetime.time(17, 51, 54, 679421))),
                ('herramienta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mUP_herramienta.herramienta')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mUP_herramienta.tipomantenimientoherramienta')),
            ],
        ),
    ]
