# Generated by Django 5.0.3 on 2024-06-11 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0003_alter_package_functions_alter_package_package_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='amount',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='package',
            name='calling_software',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='crm',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='ticket_software',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='user_administration',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
