# Generated by Django 5.0.3 on 2024-06-11 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0004_alter_package_amount_alter_package_calling_software_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='crm',
            field=models.CharField(blank=True, max_length=1300, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='user_administration',
            field=models.CharField(blank=True, max_length=1300, null=True),
        ),
    ]