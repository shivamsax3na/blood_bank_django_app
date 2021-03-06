# Generated by Django 3.1.4 on 2021-02-09 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodBankApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='body',
        ),
        migrations.AddField(
            model_name='post',
            name='bloodgroup',
            field=models.CharField(blank=True, choices=[('O-Positive', 'O-Positive'), ('O-Negative', 'O-Negative'), ('A-Positive', 'A-Positive'), ('A-Negative', 'A-Negative'), ('B-Positive', 'B-Positive'), ('B-Negative', 'B-Negative'), ('AB-Positive', 'AB-Positive'), ('AB-Negative', 'AB-Negative')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='email',
            field=models.EmailField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='phone',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
