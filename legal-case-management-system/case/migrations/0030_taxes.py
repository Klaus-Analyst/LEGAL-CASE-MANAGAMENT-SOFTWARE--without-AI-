# Generated by Django 4.1.2 on 2023-02-27 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0029_services_rename_service_name_judge_judge_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='taxes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax_name', models.CharField(blank=True, max_length=100, null=True)),
                ('percentage', models.IntegerField(blank=True, null=True)),
                ('detail', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]