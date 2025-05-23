# Generated by Django 5.2 on 2025-05-09 18:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project2', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='fkey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project2.student'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default=2, upload_to='profile_images/'),
            preserve_default=False,
        ),
    ]
