# Generated by Django 3.2.6 on 2021-11-30 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parametres', '0002_alter_technicien_email'),
        ('engins', '0002_auto_20211130_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='moto',
            name='projet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parametres.projet'),
        ),
    ]