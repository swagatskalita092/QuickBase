# Generated by Django 4.2.2 on 2023-08-01 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('googledriveapp', '0003_remove_file_file_type_alter_file_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
