# Generated by Django 4.1.2 on 2023-02-28 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0046_admin_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]