# Generated by Django 4.0.2 on 2022-06-15 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinput',
            name='cUserTemporarilyScore',
            field=models.CharField(blank=True, default='0', max_length=255),
        ),
    ]
