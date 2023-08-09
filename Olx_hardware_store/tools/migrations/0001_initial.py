# Generated by Django 4.2.3 on 2023-08-08 19:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('tool_photo', models.URLField()),
                ('description', models.TextField(max_length=200)),
                ('tool_country', models.CharField(max_length=30)),
                ('tool_city', models.CharField(max_length=50)),
                ('tool_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
