# Generated by Django 4.2.3 on 2023-08-09 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='last_edit',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
