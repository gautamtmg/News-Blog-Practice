# Generated by Django 3.1.7 on 2021-04-05 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='isEditorPick',
            field=models.BooleanField(default=False),
        ),
    ]
