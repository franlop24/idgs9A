# Generated by Django 4.0.5 on 2022-06-29 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipoJWN', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bar',
            options={'ordering': ['-nombre'], 'verbose_name': 'bar', 'verbose_name_plural': 'barres'},
        ),
        migrations.AlterModelOptions(
            name='cancion',
            options={'ordering': ['-nombre'], 'verbose_name': 'cancion', 'verbose_name_plural': 'canciones'},
        ),
        migrations.AlterModelOptions(
            name='pueblomagico',
            options={'ordering': ['-nombre'], 'verbose_name': 'pueblo magico', 'verbose_name_plural': 'pueblos magicos'},
        ),
        migrations.RemoveField(
            model_name='pueblomagico',
            name='ubicacion',
        ),
    ]
