# Generated by Django 3.0 on 2021-04-11 14:14

import base.functions
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MySchool',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('alt', models.CharField(max_length=35, verbose_name='Nomi')),
                ('image', models.ImageField(upload_to='', verbose_name='Rasm')),
            ],
            options={
                'verbose_name': 'Mening Maktabim',
                'verbose_name_plural': 'Mening Maktabim',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=150, verbose_name='Sarlavha')),
                ('description', models.CharField(max_length=350, verbose_name="Ta'rif")),
                ('image', models.ImageField(upload_to=base.functions.upload_image, verbose_name='Maqola uchun rasm')),
                ('body', models.TextField(verbose_name="To'liq matn")),
            ],
            options={
                'verbose_name': 'Yangiliklar',
                'verbose_name_plural': 'Yangiliklar',
            },
        ),
        migrations.CreateModel(
            name='OnlineService',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=80, verbose_name='title')),
                ('description', models.CharField(max_length=200, verbose_name='tarif')),
                ('link', models.URLField(max_length=80)),
                ('icon', models.CharField(choices=[('bx bxl-dribbble', 'sport'), ('bx bx-file', 'hujjatlar'), ('bx bx-world', 'web'), ('bx bx-git-branch', 'linklar')], max_length=80)),
            ],
            options={
                'verbose_name': 'Online Xizmatlar',
                'verbose_name_plural': 'Online Xizmatlar',
            },
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=50, verbose_name='muallif')),
                ('body', models.TextField(verbose_name='Maqol')),
            ],
            options={
                'verbose_name': 'Maqollar',
                'verbose_name_plural': 'Maqollar',
            },
        ),
        migrations.CreateModel(
            name='School_info',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, verbose_name='School email')),
                ('location', models.CharField(max_length=200)),
                ('all_children', models.PositiveIntegerField(verbose_name='All Childrens')),
                ('all_team', models.PositiveIntegerField(verbose_name='All Teachers')),
                ('all_classes', models.PositiveIntegerField(verbose_name='All classes')),
                ('all_extra_lessons', models.PositiveIntegerField(verbose_name='All extra lessons')),
            ],
            options={
                'verbose_name': 'School info',
                'verbose_name_plural': 'School info',
            },
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Obuna',
                'verbose_name_plural': 'Obunalar',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('surename', models.CharField(max_length=80)),
                ('jobs', models.CharField(max_length=80, verbose_name='Lavozim')),
                ('contact', models.EmailField(blank=True, max_length=254, null=True)),
                ('image', models.ImageField(upload_to=base.functions.upload_image)),
                ('telegram', models.URLField(blank=True, null=True)),
                ('instagaram', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': "Maktab o'qituvchisi",
                'verbose_name_plural': "Maktab o'qituvchilari",
            },
        ),
    ]
