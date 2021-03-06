# Generated by Django 3.2.6 on 2021-11-30 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parametres', '0002_alter_technicien_email'),
        ('engins', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moto',
            name='responsable',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parametres.technicien'),
        ),
        migrations.AddField(
            model_name='vehicule',
            name='projet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parametres.projet'),
        ),
    ]
