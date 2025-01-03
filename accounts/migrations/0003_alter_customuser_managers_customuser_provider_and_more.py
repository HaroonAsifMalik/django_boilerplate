# Generated by Django 5.1.3 on 2025-01-02 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_customuser_username'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='provider',
            field=models.CharField(blank=True, choices=[('google', 'google')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='user_images/'),
        ),
    ]
