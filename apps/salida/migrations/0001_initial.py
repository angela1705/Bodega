# Generated by Django 5.1 on 2024-09-20 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Salida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('categoria', models.CharField(choices=[('educativos', 'Educativos'), ('ropa', 'Ropa'), ('cosmeticos', 'Cosmeticos')], max_length=50)),
                ('fechaSalida', models.DateField(auto_now_add=True)),
                ('cantidad', models.IntegerField()),
            ],
        ),
    ]