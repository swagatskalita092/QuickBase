# Generated by Django 4.2.2 on 2023-07-28 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('googledriveapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='file_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='files/'),
        ),
    ]
