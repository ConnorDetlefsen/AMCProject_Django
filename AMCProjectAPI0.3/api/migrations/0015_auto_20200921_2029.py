# Generated by Django 3.1.1 on 2020-09-21 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20200919_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question2',
            field=models.TextField(blank=True, max_length=364, null=True),
        ),
    ]
