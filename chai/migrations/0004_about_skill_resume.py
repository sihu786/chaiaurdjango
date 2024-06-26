# Generated by Django 5.0.6 on 2024-06-23 05:20

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0003_chaicertificate_chaireview_store'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_heading', models.CharField(max_length=100)),
                ('personal_info', models.CharField(max_length=500)),
                ('date_of_birth', models.CharField(max_length=25)),
                ('age', models.IntegerField()),
                ('website', models.CharField(max_length=50)),
                ('phone_no', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=256)),
                ('city', models.CharField(max_length=50)),
                ('freelance', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='profile/')),
                ('about_me', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_skill', models.TextField()),
                ('htlm', models.IntegerField()),
                ('css', models.IntegerField()),
                ('java_script', models.IntegerField()),
                ('python', models.IntegerField()),
                ('django', models.IntegerField()),
                ('linux', models.IntegerField()),
                ('about', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='chai.about')),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_degree', models.TextField()),
                ('year', models.TextField()),
                ('institute_name_and_address', models.TextField()),
                ('skill', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='chai.skill')),
            ],
        ),
    ]
