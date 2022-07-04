# Generated by Django 4.0.4 on 2022-05-31 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chofer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('nacimiento', models.DateField()),
                ('movil_a_cargo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('registro', models.DateField()),
                ('movil_asignado', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Movil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patente', models.CharField(max_length=40)),
                ('marca', models.CharField(max_length=40)),
                ('modelo', models.DateField()),
                ('chofer_asignado', models.IntegerField()),
            ],
        ),
    ]