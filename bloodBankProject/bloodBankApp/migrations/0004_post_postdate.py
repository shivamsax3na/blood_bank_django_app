# Generated by Django 3.1.6 on 2021-02-16 15:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bloodBankApp', '0003_auto_20210209_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='postDate',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]