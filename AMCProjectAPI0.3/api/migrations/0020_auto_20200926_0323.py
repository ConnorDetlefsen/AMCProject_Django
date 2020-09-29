# Generated by Django 3.1.1 on 2020-09-26 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20200926_0316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='question1',
        ),
        migrations.RemoveField(
            model_name='user',
            name='question2',
        ),
        migrations.RemoveField(
            model_name='user',
            name='question3',
        ),
        migrations.RemoveField(
            model_name='user',
            name='question4',
        ),
        migrations.AddField(
            model_name='user',
            name='quizResults',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.quizresults'),
        ),
    ]
