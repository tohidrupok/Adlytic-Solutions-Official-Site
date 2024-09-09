# Generated by Django 5.0.3 on 2024-09-09 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0012_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
        ),
    ]