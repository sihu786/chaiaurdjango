# Generated by Django 5.0.6 on 2024-06-23 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0004_about_skill_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='degree',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='about',
            name='about_me',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='about',
            name='personal_info',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='resume',
            name='institute_name_and_address',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='resume',
            name='year',
            field=models.CharField(max_length=5),
        ),
    ]
