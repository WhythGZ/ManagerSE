# Generated by Django 4.1.3 on 2022-11-30 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0009_cita_alter_marca_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marca',
            name='logo',
        ),
        migrations.AddField(
            model_name='marca',
            name='imgMarca',
            field=models.ImageField(null=True, upload_to='marca'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
