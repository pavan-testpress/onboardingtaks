# Generated by Django 2.1.3 on 2018-12-20 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccountsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccounts',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], default='', max_length=1),
        ),
    ]
