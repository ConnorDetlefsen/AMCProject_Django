# Generated by Django 3.1.1 on 2020-09-29 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_questiontracking'),
    ]

    operations = [
        migrations.AddField(
            model_name='questiontracking',
            name='correct',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
