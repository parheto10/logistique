# Generated by Django 3.2.13 on 2022-06-24 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipements', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imprimante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=225)),
                ('numero_serie', models.CharField(max_length=225)),
                ('marque', models.CharField(choices=[('ASUS', 'ASUS'), ('DELL', 'DELL'), ('HP', 'HP')], max_length=225)),
                ('model', models.CharField(blank=True, max_length=225, null=True)),
                ('utilisateur', models.CharField(max_length=225)),
                ('date_achat', models.DateField(blank=True, null=True)),
                ('prix_achat', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'imprimantes',
                'verbose_name_plural': 'IMPRIMANTES',
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='Ordinateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=225)),
                ('numero_serie', models.CharField(max_length=225)),
                ('marque', models.CharField(choices=[('ASUS', 'ASUS'), ('DELL', 'DELL'), ('HP', 'HP')], max_length=225)),
                ('model', models.CharField(blank=True, max_length=225, null=True)),
                ('utilisateur', models.CharField(max_length=225)),
                ('date_achat', models.DateField(blank=True, null=True)),
                ('prix_achat', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'ordinateurs',
                'verbose_name_plural': 'ORDNATEURS',
                'ordering': ['code'],
            },
        ),
    ]