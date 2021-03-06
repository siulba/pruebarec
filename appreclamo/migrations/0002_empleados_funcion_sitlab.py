# Generated by Django 3.0.5 on 2021-01-20 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appreclamo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70, null=True, unique=True)),
                ('observacion', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Sitlab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, null=True, unique=True)),
                ('observacion', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('numdoc', models.CharField(max_length=12)),
                ('domicilio', models.CharField(blank=True, max_length=80)),
                ('telef', models.CharField(blank=True, max_length=12)),
                ('turno', models.CharField(blank=True, max_length=30)),
                ('cuil', models.CharField(blank=True, max_length=12)),
                ('Fecha_nac', models.DateField(null=True)),
                ('observacion', models.CharField(blank=True, max_length=150)),
                ('cod_func', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appreclamo.Funcion', to_field='nombre')),
                ('cod_sitlab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appreclamo.Sitlab', to_field='nombre')),
            ],
        ),
    ]
